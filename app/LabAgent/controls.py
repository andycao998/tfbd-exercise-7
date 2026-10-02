from aws_config import get_client

GUARDRAIL_ID = "dbhb9o00o9zb" # would usually go in .env


# allow-list
PARTNER_MAY_SEE = {"booking_id", "booking_date", "name"}


def for_partner(record: dict) -> dict:
    """ Mask PII for partner using guardrail. """

    text = str(record)

    response = get_client("bedrock-runtime").apply_guardrail(
        guardrailIdentifier=GUARDRAIL_ID,
        guardrailVersion="DRAFT",
        source="INPUT",
        content=[{"text": {"text": text}}]
    )

    if response["action"] == "GUARDRAIL_INTERVENED":
        raise ValueError("Outbound payload rejected by privacy guardrail")

    return text



def _entities(text: str):
    """ Comprehend PII entities in the text."""
    if not text or not text.strip():
        return []

    comprehend = get_client("comprehend")
    return comprehend.detect_pii_entities(Text=text, LanguageCode="en")["Entities"]


def comprehend_helper(text: str) -> str:
    """ Replace PII the partner isn't allowed to see. """

    if not text:
        return text

    result = text
    for entity in sorted(_entities(text), key=lambda e: e["BeginOffset"], reverse=True): # start backwards
        if entity["Type"] in PARTNER_MAY_SEE:
            continue

        result = {
            result[:entity["BeginOffset"]] + # every thing up to redacted + placeholder + every thing after
            f"[{entity["Type"]}]" +
            result[entity["EndOfsset"]:]
        }

    return result


# This storage allow-list keeps only non-sensitive booking facts for durable writes.
STORAGE_ALLOW = {"booking_id", "booking_date", "status"}


def for_storage(value: list | dict | str, _depth=0) -> list | dict | str:
    """ Drop fields that aren't allow-listed, before the record is written. """

    if _depth > 6: # should never reach this depth for this exercise but good to have
        return "[nested]"

    if isinstance(value, dict):
        out = {}
        for key, item in value.items():
            if key in STORAGE_ALLOW:
                out[key] = for_storage(item, _depth + 1)
            elif isinstance(item, (dict, list)):
                out[key] = for_storage(item, _depth + 1)
            else:
                out[key] = "[removed]"
        
        return out

    if isinstance(value, list):
        return [for_storage(item, _depth + 1) for item in value]

    if isinstance(value, str):
        return comprehend_helper(value) # use comprehend to handle the strings

    return value
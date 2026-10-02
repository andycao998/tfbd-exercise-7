import datetime
import json

from controls import for_storage


TRANSCRIPT = "booking_log.jsonl"


def log(event, payload):
    """ Append one line to the transcript. """

    with open(TRANSCRIPT, "a", encoding="utf-8") as handle:
        handle.write(
            json.dumps(
                {
                    "ts": datetime.now(datetime.timezone.utc).isoformat(),
                    "event": event,
                    "payload": for_storage(payload)
                }
            )
            + "\n"
        )

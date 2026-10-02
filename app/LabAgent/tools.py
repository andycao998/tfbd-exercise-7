from langchain.tools import tool
from controls import for_partner


BOOKINGS = [
    {
        "booking_id": "AIUA24DJAI",
        "booking_date": "2026-10-12",
        "name": "Bill Walker",
        "phone_number": "123-456-7890",
        "email": "bwalker@gmail.com" 
    }, 
    {
        "booking_id": "JKF4HDAU81",
        "booking_date": "2026-11-20",
        "name": "Alisha Torres",
        "phone_number": "987-654-3210",
        "email": "atorres@gmail.com",
    },
    {
        "booking_id": "VN7B2BAK90",
        "booking_date": "2026-12-01",
        "name": "Hailey King",
        "phone_number": "123-654-7810",
        "email": "hking@gmail.com"
    }
]


@tool
def read_record(booking_id: str) -> dict[str, str]:
    """Look up a booking record from the fake backing store."""
    lookup = booking_id.upper()

    for booking in BOOKINGS:
        if booking.get("booking_id", "").upper() == lookup:
            return booking
        
    return {"status": "NO_BOOKING_FOUND"}


THIRD_PARTY_DATA: list[dict[str, str]] = []


@tool
def send_contact_detail(contact: dict[str, str]) -> dict[str, str]:
    """ Send only the partner-approved contact fields to a simulated third party. """
    sanitized_contact = for_partner(contact)
    THIRD_PARTY_DATA.append(sanitized_contact)

    return {"status": "SENT"}


TOOLS = [read_record, send_contact_detail]
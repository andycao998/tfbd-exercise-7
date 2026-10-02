# Clinic Booking Privacy Lab

This project implements a small clinic-booking assistant running on AgentCore Runtime. It reads a fake patient booking record, forwards only the minimal partner-approved subset, and writes sanitized booking facts to disk without raw PII.


## Disclaimer
I wasn't able to finish or even test the functionality of this lab. If I had another day, I would start with testing the functionality in agentcore dev and making sure it ran. After confirming it works as intended, I would work on tests and FINDINGS.md


## Run locally
`agentcore dev`

## Relevant files

- `app/LabAgent/controls.py` - `for_partner()` and `for_storage()`
- `app/LabAgent/tools.py` - fake backing-store lookup and outbound contact tool
- `app/LabAgent/store.py` - sanitized persistence helper
- `FINDINGS.md` - the required evaluation write-up

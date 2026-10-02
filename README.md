# Clinic Booking Privacy Lab

This project implements a small clinic-booking assistant running on AgentCore Runtime. It reads a fake patient booking record, forwards only the minimal partner-approved subset, and writes sanitized booking facts to disk without raw PII.


## Disclaimer
I made progress on stubbing out my code and getting the `agentcore dev` environment to launch, but I ran out of time. I was not able to test any functionality I wrote for this lab. If I had another day, I would start with testing in `agentcore dev` and making sure it ran. This includes confirming I can connect to the Bedrock Guardrail I created and AWS Comprehend. After confirming it works as intended, I would work on tests for the leaks to confirm PII is handed in all cases. Finally, I would write my findings in FINDINGS.md.


## Run locally
`agentcore dev`

## Relevant files

- `app/LabAgent/controls.py` - `for_partner()` and `for_storage()`
- `app/LabAgent/tools.py` - fake backing-store lookup and outbound contact tool
- `app/LabAgent/store.py` - sanitized persistence helper
- `FINDINGS.md` - the required evaluation write-up

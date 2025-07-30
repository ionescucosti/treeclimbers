## Task

Build a simple backend API that receives job requests and:
- Processes each request only once, even if submitted multiple times
- Assigns each valid request to one of three “workers”
- Saves the result to a database

## Requirements

Implement the following endpoint:

### POST /process-request

Accepts a request:
JSON
{
  "request_id": "abc123",  
  "payload": { "some": "data"}}
  
tech required: fastapi, sqlalchemy, redis

### How to start the app:
- ex: run python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
- open http://127.0.0.1:8000/docs#/default/ to see available endpoints
- open http://127.0.0.1:8000/docs#/default/process_request_process_request_post to test it

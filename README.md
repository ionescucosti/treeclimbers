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

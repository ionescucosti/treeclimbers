from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .schemas import JobRequestIn
from .models import JobRequest
from .database import SessionLocal, engine, Base
from .redis_client import redis_client
from .worker_assignment import assign_worker

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/process-request")
def process_request(request: JobRequestIn, db: Session = Depends(get_db)):
    if redis_client.get(request.request_id):
        raise HTTPException(status_code=409, detail="Request already processed")

    redis_client.set(request.request_id, "processed")

    worker = assign_worker(request.request_id)
    job = JobRequest(request_id=request.request_id, payload=request.payload, worker=worker)
    db.add(job)
    db.commit()

    return {"status": "processed", "worker": worker}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

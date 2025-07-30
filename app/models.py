from sqlalchemy import Column, String, JSON
from .database import Base

class JobRequest(Base):
    __tablename__ = "job_requests"
    request_id = Column(String, primary_key=True, index=True)
    payload = Column(JSON)
    worker = Column(String)

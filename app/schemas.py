from pydantic import BaseModel
from typing import Dict

class JobRequestIn(BaseModel):
    request_id: str
    payload: {str: str}

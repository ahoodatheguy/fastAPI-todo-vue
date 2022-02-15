from typing import Optional
from pydantic import BaseModel


class NewTask(BaseModel):
	name: str
	desc: Optional[str] = None

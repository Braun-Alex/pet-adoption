from pydantic import BaseModel
from typing import Optional


class UserLocal(BaseModel):
    id: Optional[str] = None
    email: str
    full_name: Optional[str] = None
    password: str
    salt: Optional[str] = None

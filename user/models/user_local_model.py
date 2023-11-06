from pydantic import BaseModel
from typing import Optional

class UserLocal(BaseModel):
    id: Optional[int] = None
    email: Optional[str] = None
    full_name: Optional[str] = None
    password: Optional[str] = None
 
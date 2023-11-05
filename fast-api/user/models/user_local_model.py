from pydantic import BaseModel
from typing import Optional

class UserLocal(BaseModel):
    id: Optional[int]
    email: Optional[str]
    full_name: Optional[str]
    password: Optional[str]
 
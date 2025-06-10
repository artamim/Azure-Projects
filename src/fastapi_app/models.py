from pydantic import BaseModel

class Item(BaseModel):
    id: str
    name: str
    description: str
    is_complete: bool
from pydantic import BaseModel

class Contact(BaseModel):
    name:str
    contact_no:str
from bll.contacts_bll import ContactsBll
from fastapi import APIRouter
from domain.contact import Contact

router = APIRouter(tags=["Contacts API"])
contact_bll = ContactsBll("json")

@router.get("/contacts")
def display_contacts():
    return contact_bll.retrieve_contacts().get("contacts", [])

@router.get("/contacts/search")
def search_contacts(keyword:str)->list[Contact]:
    return contact_bll.search_contacts(keyword).get("contacts", [])

# @router.get("/contacts/search/{keyword}")
# def search_contacts(keyword:str)->list[Contact]:
#     return contact_bll.search_contacts(keyword).get("contacts", [])

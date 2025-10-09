from bll.contacts_bll import ContactsBll
from fastapi import APIRouter
from domain.contact import Contact
from domain.service_response import ServiceResponse
from util.logger import enable_logging, Logger

router = APIRouter(tags=["Contacts API"])
contact_bll = ContactsBll("json")


@router.get("/contacts")
@enable_logging
def display_contacts()->ServiceResponse[list[Contact]]:
    response = ServiceResponse()
    try:
        response.data = contact_bll.retrieve_contacts().get("contacts", [])
    except Exception as ex:
        response.status_code = 500
        response.status_message = str(ex)

    return response

@router.get("/contacts/search")
@enable_logging
def search_contacts(keyword:str)->list[Contact]:
    return contact_bll.search_contacts(keyword).get("contacts", [])

# @router.get("/contacts/search/{keyword}")
# def search_contacts(keyword:str)->list[Contact]:
#     return contact_bll.search_contacts(keyword).get("contacts", [])

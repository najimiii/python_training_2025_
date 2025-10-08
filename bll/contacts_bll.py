
from dal.abstract_contacts import ContactsABC
from dal.dal_factory import ContactsFactory

class ContactsBll:

    def __init__(self,source):
        self.__contact_dao:ContactsABC = ContactsFactory().create_instance(source)

    def retrieve_contacts(self):
        return self.__contact_dao.retrieve_contacts()
    
    def search_contacts(self, keyword):
        return self.__contact_dao.search_contacts(keyword)

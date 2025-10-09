
from dal.abstract_contacts import ContactsABC
from dal.dal_factory import ContactsFactory
from util.logger import enable_logging
from domain.contact import Contact

class ContactsBll:

    def __init__(self,source):
        self.__contact_dao:ContactsABC = ContactsFactory().create_instance(source)

    @enable_logging
    def retrieve_contacts(self)->list[Contact]:
        result:list[Contact] = []
        for record in self.__contact_dao.retrieve_contacts().get("contacts", []):
            result.append(Contact(name=record['name'], contact_no=record['contact_no']))
        # raise Exception("Error in business layer")
        return result
    
    @enable_logging
    def search_contacts(self, keyword):
        return self.__contact_dao.search_contacts(keyword)

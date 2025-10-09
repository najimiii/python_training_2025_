from util.file_util import read_json_as_dict
from dal.abstract_contacts import ContactsABC
from util.logger import enable_logging 

class ContactsJsonDao(ContactsABC):
    @enable_logging
    def retrieve_contacts(self):
        return read_json_as_dict("contacts.json")
    
    @enable_logging
    def search_contacts(self, keyword):
        result = {
            "contacts": []
        }

        for record in self.retrieve_contacts().get("contacts", []):
            if record.get("name").find(keyword) >= 0:
                result.get("contacts").append(record) 
        return result
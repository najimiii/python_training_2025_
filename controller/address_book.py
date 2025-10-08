from bll.contacts_bll import ContactsBll

class Contacts:

    def __init__(self, source="json"):
        self.contacts_bll = ContactsBll(source)

    def display_contacts(self):
        self.__do_display_result(self.contacts_bll.retrieve_contacts().get("contacts", []))
    
    def search_contacts(self,keyword):
        self.__do_display_result(self.contacts_bll.search_contacts( keyword).get("contacts", []))

    def __do_display_result(self, records):
        for record in records:
            print(f"Name:{record.get('name', " ")} Phone #: {record.get('phone')}")
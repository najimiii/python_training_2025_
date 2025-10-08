
from dal.db_dal import DbDaoABC
from dal.abstract_contacts import ContactsABC


class ContactsDbDao(DbDaoABC, ContactsABC):
        

    def retrieve_contacts(self):
        sql = "select name, phone from contacts"
        results = {"contacts": []}
        for row in self.execute_select(sql):
            results.get("contacts").append({"name": row[0], "phone": row[1]})

        return results
    
    def search_contacts(self, keyword):
        return Exception("Not implemented")
    
    
    
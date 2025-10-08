
from controller.address_book import Contacts

try:
    Contacts("json").search_contacts("Jane")
    #Contacts().display_contacts("db")

except Exception as ex:
    print(f"Error in starting application:{str(ex)}")
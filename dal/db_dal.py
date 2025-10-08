import sqlite3
import os

class DbDaoABC:
    

    def _get_db_connection(self):
        db_path = os.path.join(os.path.dirname(__file__), "address_book.db")
        return sqlite3.connect(db_path)
    
    def execute_select(self, sql):
        cnn = self._get_db_connection()
        return cnn.execute(sql)

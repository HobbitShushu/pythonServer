from application import dbconfig
import mysql.connector

class dbCommander(object):
    def __init__(self, conn_cursor, conn):
        self.cursor = conn_cursor
        self.conn = conn

    def start_transaction(self):
        self.conn.start_transaction(False, 'READ COMMITTED')

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def execute(self, query, args):
        self.cursor.execute(query, args)

        self.cursor_stored_data = []
        for row in self.cursor:
            self.cursor_stored_data.append(dict(zip(self.cursor.column_names, row)))
        return self.cursor_stored_data

class dbConnector(object):
    def __init__(self, readOnly = False, transaction = False):
        self.conn = mysql.connector.connect(**dbconfig['Setting'])
        print(self.conn)
    
    def __enter__(self):
        self.conn_cursor = self.conn.cursor()
        self.dbCommander = dbCommander(self.conn_cursor, self.conn)
        
        # if self.transaction:
        #    self.dbCommander.start_transaction()

        return self.dbCommander

    def __exit__(self, type, value, traceback):
        self.dbCommander.commit()   
        self.conn_cursor.close()
        self.conn.close()
        
import sqlite3

class SqliteLogger(object):
    def __init__(self, database, table):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        self.table = table
        self.cursor.execute('''CREATE TABLE  IF NOT EXISTS {}(
                               id INTEGER PRIMARY KEY,
                               class INTEGER,
                               timestamp UNSIGNED BIGINT)'''.format(table))
        self.connection.commit()


    def log(self, class_number, timestamp):
        self.cursor.execute('''INSERT INTO {} (class, timestamp)
                              VALUES ({}, {})'''.format(self.table, class_number, timestamp))
        self.connection.commit()
        
    def __enter__(self):
         return self


    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()
    

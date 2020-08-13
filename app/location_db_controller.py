import sqlite3

class Database:
    
    def create_connection(self):
        conn = None
        # Attempts to connect to the database
        try:
            conn = sqlite3.connect('locations.db')
        except:
            print('Could not connect to locations.db')
        return conn
    
    def get_all_locations(self):
        rows = None
        try:
            conn = self.create_connection()
            cur = conn.cursor()
            cur.execute('SELECT * FROM user_locs')
            rows = cur.fetchall()
        except:
            print("Errror getting all entries in the DB")
        return rows    
import sqlite3

class Database:

    def __init__(self):
        self.setup()
    
    def setup(self):
        print("Setting up table")
        sql_statement = """CREATE TABLE IF NOT EXISTS user_locs (user_id INTEGER NOT NULL PRIMARY KEY, country_code TEXT); """
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute(sql_statement)
        conn.commit()
        conn.close()
    
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
            conn.close()
        except:
            print("Errror getting all entries in the DB")
        return rows    
    
    def insert_location(self, user_id, country_code):
        # Attempts to insert a new entry in the database
        try:
            sql_statement = f'INSERT INTO user_locs VALUES ({user_id}, "{country_code}");'
            conn = self.create_connection()
            cur = conn.cursor()
            cur.execute(sql_statement)
            conn.commit()
            conn.close()
            return 'insert success' 
        # Catches the exception that the id already exists and then triggers an update instead
        except sqlite3.IntegrityError:
            sql_statement = f'UPDATE user_locs SET country_code = "{country_code}" WHERE user_id = {user_id};'
            conn = self.create_connection()
            cur = conn.cursor()
            cur.execute(sql_statement)
            conn.commit()
            conn.close()
            return 'update success'
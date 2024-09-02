import uuid
import mysql.connector

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="rikzon"
        )
        self.cursor = self.connection.cursor()

    
    def signup(self, username, password):
        try:
            insert_user_query = "INSERT INTO user(username, password) VALUES(%s, %s)"
            self.cursor.execute(insert_user_query, (username, password))
            self.connection.commit()
            return True
        except mysql.connector.IntegrityError:
            return False

        
    def check_user(self, username, password):
        check_user_query = "SELECT * FROM user WHERE username = %s AND password = %s"
        self.cursor.execute(check_user_query, (username, password))
        user = self.cursor.fetchone()
        if user:
            return True
        else:
            return False
    
    def close_db_connection(self):
         self.con.close()

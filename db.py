import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",       # replace with your MySQL username
        password="9225",  # replace with your MySQL password
        database="skillsdb"
    )

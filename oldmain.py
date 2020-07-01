import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv('USERNAME')
DB_PASSWORD = os.getenv('PASSWORD')
DB_DATABASE = os.getenv('DATABASE')

mydb = mysql.connector.connect(
  host="localhost",
  user=DB_USER,
  password=DB_PASSWORD,
  database=DB_DATABASE
)

def new_server(mycursor):
    mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), discord_id VARCHAR(255), date_registered VARCHAR(255), level DOUBLE, experience INT, messages INT)")

def insert_user(mycursor, name, discord_id, lvl, exp, msgs, date_reg):
    insert = f"INSERT INTO users (name, discord_id, level, experience, messages) VALUES ({name}, {discord_id}, {lvl}, {exp}, {msgs}, {date_reg})"
    mycursor.execute(insert)

mycursor = mydb.cursor()
# mycursor.execute("SHOW DATABASES")
mycursor.execute("DROP table users;")
# mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), discord_id VARCHAR(255), date_registered VARCHAR(255), level DOUBLE, experience INT, messages INT)")
# insert = "INSERT INTO users (name, discord_id, date_registered, level, experience, messages) VALUES (%s, %s, %s, %s, %s, %s)"
# data = [
#     ("User 1", "2131245451", "2020-3-20", 10, 4000, 30),
#     ("User 2", "43509883409", "2010-2-11", 23, 8000, 230),
#     ("User 3", "2319081222", "2002-10-29", 2, 210, 2)
# ]

# mycursor.executemany(insert, data)
mydb.commit()
print(mycursor.rowcount, "values were inserted.")
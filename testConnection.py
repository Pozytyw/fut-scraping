import mysql.connector
import test
from mysql.connector import errorcode

#connet to db
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="root",
    port="3306",
    database="cyganeria"
)

#create cursor
cursor = mydb.cursor(dictionary=True)
try:
    cursor.execute("select * from players")
except mysql.connector.Error as err:
    print("error " + err)
    exit(1)
x = cursor.fetchall()

for elem in x:
    print(x)
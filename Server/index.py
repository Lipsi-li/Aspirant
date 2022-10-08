#!C:\Users\No_name\AppData\Local\Programs\Python\Python310\python.exe
import cgi

import mysql.connector

print("Content-type: text/html")
print()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gps_location"
)

getparam = cgi.FieldStorage()
get_location = getparam.getfirst("local", "0")


mycursor = mydb.cursor()

sql = "INSERT INTO gps_data (gps_localtion_data, trash) VALUES (%s, %s)"
val = (get_location, 'success')
mycursor.execute(sql, val)


mydb.commit()

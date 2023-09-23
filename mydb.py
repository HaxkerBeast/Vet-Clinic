import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Sanskar@12'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE vetclinic")

print("ALL DONE")
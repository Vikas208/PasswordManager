from GetPassword import Password
import mysql.connector


def CreateDatabase():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=Password()
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE PASSWORD_MANAGER")
        # print("DATABASE CREATED")
    except Exception as e:
        pass
        # print(e)

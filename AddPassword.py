from GetPassword import Password
import mysql.connector


def ADD_RECORD():

    try:

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=Password(),
            database="PASSWORD_MANAGER"
        )

        mycursor = mydb.cursor()

        # CHECK TABLE IS AVAILABLE OR NOT
        mycursor.execute('''SELECT COUNT(*)
                         FROM information_schema.tables
                         WHERE table_schema='password_manager'
                         AND table_name='passmanager'
                         ''')
        counter = 0
        for x in mycursor:
            counter = x
        if 0 in counter:
            mycursor.execute(
                "CREATE TABLE PASSMANAGER(ID INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY ,SITENAME VARCHAR(100) NOT NULL,  PASSWORD VARCHAR  (100) NOT NULL)")

        sitename = input("ENTER SITE NAME: ")
        password = input("ENTER PASSWORD: ")

        while (sitename == " ") or (password == "   "):
            sitename = input("PLEASE ENTER  SITE     NAME:")
            password = input("ENTER PASSWORD: ")

        sql = f"INSERT INTO PASSMANAGER (SITENAME,PASSWORD) VALUES ('{sitename}','{password}')"
        mycursor.execute(sql)
        mydb.commit()
        print("Password Saved")
        # print(mycursor.rowcount, "record inserted")
    except Exception as e:
        print(e)

from GetPassword import Password
import mysql.connector


def searchData():
    try:

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=Password(),
            database="PASSWORD_MANAGER"
        )

        mycursor = mydb.cursor()
        mycursor.execute('''SELECT COUNT(*)
                         FROM information_schema.tables
                         WHERE table_schema='PASSWORD_MANAGER'
                         AND table_name='PASSMANAGER'
                         ''')
        counter = 0
        for x in mycursor:
            counter = x
        if 0 in counter:
            print("No DataBase Found\nPlease Add Passwords")
        else:
            sitename = input("Enter Site Name: ")
            counter = 0
            sql = f"SELECT * FROM PASSMANAGER WHERE SITENAME like '%{sitename}%'"
            mycursor.execute(sql)
            for x in mycursor:
                counter += 1
                print(x)
            if(counter == 0):
                print("No Data found")

    except Exception as e:
        print(e)

from GetPassword import Password
import mysql.connector


def Modifypassword():
    try:
        sitename = input("Enter Site Name: ")
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=Password(),
            database="PASSWORD_MANAGER"
        )
        mycursor = mydb.cursor()
        sql = f"select ID,SITENAME  from PASSMANAGER where sitename like '%{sitename}%'"
        mycursor.execute(sql)

        counter = 0
        for x in mycursor:
            counter = 1
            print(x)
        if(counter == 0):
            print("SiteName not found")
        else:
            selection = int(input("choose which site do you want to modify "))
            print("Enter New Details")
            sitename = input("Enter Site Name:")
            password = input("Enter Password: ")
            sql = f"update PASSMANAGER set sitename='{sitename}',password='{password}' where id={selection}"
            mycursor.execute(sql)
            print(mycursor.rowcount, " Record Modified")
            mydb.commit()
    except Exception as e:
        print(e)

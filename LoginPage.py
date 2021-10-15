from GetPassword import Password
import mysql.connector


def Login():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=str(Password()),
            database="PASSWORD_MANAGER"
        )

        mycursor = mydb.cursor()
        mycursor.execute('''SELECT COUNT(*)
                             FROM information_schema.tables
                             WHERE table_schema='PASSWORD_MANAGER'
                             AND table_name="SIGNUP"''')
        counter = 0
        for x in mycursor:
            counter = x
        if(counter == 0):
            print("You can't Sign up Just go for the Signup first")
        else:
            username = input("Enter Username: ")
            password = input("Enter Password: ")

            sql = f"SELECT * FROM SIGNUP WHERE USERNAME='{username}' AND PASSWORD='{password}'"
            mycursor.execute(sql)
            counter = 0
            for x in mycursor:
                counter += 1
            if counter == 0:
                print("No User name and Password found")
                return 0
            else:
                return 1
    except Exception as e:
        print(e)
        return 0

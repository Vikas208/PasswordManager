from GetPassword import Password
import mysql.connector


def signup():

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
            # print(x)
        if(0 in counter):
            username = input("Enter user name: ")
            password = input("Enter Password: ")
            while len(password) < 4:
                print("Please Enter Alteast 4 digit password")
                password = input("Enter Password: ")

            confirm = input("Confirm Password: ")
            while(confirm != password):
                print("Password not matched")
                confirm = input("Enter Password: ")
            email = input("Enter Your mail id: ")
            mycursor.execute(
                "CREATE TABLE SIGNUP (USERNAME VARCHAR(20) NOT NULL ,PASSWORD VARCHAR(10)    NOT NULL,EMAIL_ID VARCHAR(40) NOT NULL)")
            # mycursor.commit()
            sql = f"INSERT INTO SIGNUP values('{username}','{password}','{email}')"
            mycursor.execute(sql)
            mydb.commit()
            print("User Created")
        else:
            print("You have Already Account Go for the Login")
            return 1
    except Exception as e:
        print(e)
        return 0

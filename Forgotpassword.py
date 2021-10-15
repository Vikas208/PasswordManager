from GetPassword import Password
import mysql.connector


def forgot():
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
                             AND table_name="SIGNUP"''')
        cursor = 0
        for x in mycursor:
            counter = x
        if(0 in counter):
            print("No DataBase Found\nPlease first create an account")
            return 0
        else:
            emailid = input(
                "Enter Email id which you mentioned at account creation time: ")
            sql = f"SELECT * FROM SIGNUP WHERE EMAIL_ID='{emailid}'"
            mycursor.execute(sql)
            counter = 0
            for x in mycursor:
                counter = counter+1
            if(counter == 0):
                print("Email not Found")
                return 0
            else:

                while(True):

                    password = input("Enter New Password: ")
                    cpassword = input("Enter confirmed Password: ")
                    if(password == cpassword):
                        sql = f"UPDATE SIGNUP set password='{password}' WHERE   EMAIL_ID='{emailid}'"
                        mycursor.execute(sql)
                        print(mycursor.rowcount, " Record Updated")
                        mydb.commit()
                        break
                    else:
                        print("Please Enter Right Password")

    except Exception as e:
        print(e)
        return 1

from GetPassword import Password
import mysql.connector


def ShowPassword():
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
            mycursor.execute("SELECT * FROM PASSMANAGER")
            print("___________________________________")
            for x in mycursor:
                print(x)
            print("___________________________________")
    except Exception as e:
        print(e)

# ShowPassword()

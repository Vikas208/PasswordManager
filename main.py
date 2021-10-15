from AddPassword import ADD_RECORD
from CreateDatabase import CreateDatabase
from ListPassword import ShowPassword
from Searchpassword import searchData
from Signuppage import signup
from LoginPage import Login
from Forgotpassword import forgot
from DeletePassword import Deletepassword
from ModifyPassword import Modifypassword
from GenerateLogFile import GenerateLogfile


def menu():
    print("[1] Add Password              ")
    print("[2] List All Password         ")
    print("[3] Search Password           ")
    print("[4] Delete Password           ")
    print("[5] Modify Password           ")
    print("[6] Exit                      ")
    print("______________________________")


def usermenu():
    print("[1] Signup                    ")
    print("[2] Login                     ")
    print("[3] Forgot password           ")
    print("[4] Exit")
    print("______________________________")


try:
    while(1):
        CreateDatabase()
        usermenu()
        ch = int(input("Enter your choice: "))
        if ch == 1:
            signup()
            result = Login()
            if(result == 1):
                GenerateLogfile(True)
                break
        elif ch == 2:
            result = Login()
            if result == 1:
                GenerateLogfile(True)
                break
        elif ch == 3:
            c = forgot()
            if(c == 0):
                signup()
            elif c == 1:
                continue
            result = Login()
            if(result == 1):
                GenerateLogfile(True)
                break
        elif ch == 4:
            exit(0)
        else:
            print("You Select Wrong Option")

    while(1):

        menu()
        choice = int(input("Select Option: "))
        if(choice == 6):
            break
        elif choice == 1:
            ADD_RECORD()
        elif choice == 2:
            ShowPassword()
        elif choice == 3:
            searchData()
        elif choice == 4:
            Deletepassword()
        elif choice == 5:
            Modifypassword()
        else:
            print("Wrong Choice Entered")
    GenerateLogfile(False)
except Exception as err:
    print("Error")
    print(err)

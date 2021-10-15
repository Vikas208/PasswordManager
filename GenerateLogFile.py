import datetime

def GenerateLogfile(Islogin=True):
    try:
        fp = open("log.txt","a")
        if Islogin:
            fp.write(f"Login At: {datetime.datetime.now()}\n")
        else:
            fp.write(f"Logout At: {datetime.datetime.now()}\n")
        fp.close()
    except Exception as e:
        print(e)
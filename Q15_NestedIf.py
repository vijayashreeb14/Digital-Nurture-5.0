def login(user, pwd):
    if user == "":
        print("Username Empty")
        return

    if pwd == "":
        print("Password Empty")
        return

    if user == "admin":
        if pwd == "pass123":
            print("Login Successful")
        else:
            print("Invalid Password")
    else:
        print("Invalid Username")

user = "admin"
pwd = "pass123"

login(user, pwd)
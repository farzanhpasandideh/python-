for i in range(3):
    username= input("enter the username")
    password= input("enter the password")

    if username== "admin" and password=="12345":
        print("weicome")
        break
    else:
        print("Error")
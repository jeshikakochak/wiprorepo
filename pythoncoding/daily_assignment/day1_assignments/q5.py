#check if it is strong password or not
password=input("enter your password: ")
if len(password) >= 8:
    print("strong password")
else:
    print("weak password")
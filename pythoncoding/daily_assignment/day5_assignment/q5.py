text=input("enter a number:")
try:
    num=int(text)
    print("you entered:",num)
except ValueError:
    print("this is not a valid number!")
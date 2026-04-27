class NegativeNumberError(Exception):
    pass
try:
    num=float(input("enter a positive number: "))
    if num<0:
        raise NegativeNumberError("Negative number not allowed!")
    print("you entered:",num)
except NegativeNumberError as e:
    print("error:",e)
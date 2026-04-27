
try:
    a=float(input("enter first number: "))
    b=float(input("enter second number: "))
    print("result:",a/b)
except ValueError:
    print("please enter valid numbers!")
except ZeroDivisionError:
    print("cannot divide by zero!")

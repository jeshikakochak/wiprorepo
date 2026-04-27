while True:
    try:
        a=float(input("enter first number:"))
        b=float(input("enter second number:"))
        print("result:",a/b)
        break
    except ValueError:
        print("invalid input. try again")
    except ZeroDivisionError:
        print('cannot divide by zero. try aagin')
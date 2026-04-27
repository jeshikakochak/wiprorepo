def add(a,b):
    return a+b
try:
    result=add(float(input("enter first value: ")), float(input("enter second value")))
    print("sum:",result)
except ValueError:
    print("please enter numbers only!")
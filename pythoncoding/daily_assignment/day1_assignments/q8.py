#finding factorial using loops
number=int(input("enter a number: "))
factorial=1
for i in range(1,number+1):
    factorial*=i
print("factorial= ",factorial)
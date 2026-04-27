numbers=[10,20,30,40,50]
print("List:",numbers)
try:
    i=int(input("enter an index: "))
    print("element:",numbers[i])
except IndexError:
    print("Index is out of range!")
except ValueError:
    print("please enter a valid index!")
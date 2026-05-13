#date- 22/4/2026
#description- we are finding largest of two and also learning if statement
#big2
# number1 = int(input("enter a number"))
# number2 = int(input("enter another number"))
#
#
# if number1 > number2:
#     print(number1 , "is big")
# elif number1 == number2:
#     print("both are equal")
# else:
#     print(number2 , "is big")

#big3

'''num1 = int(input("enter a number"))
num2 = int(input("enter another number"))
num3 = int(input("enter third number"))

if num1==num2 and num2==num3:
    print("all values are equal")
elif num1 > num2 and num1 > num3:
    print(num1, 'num1 is biggest')
elif num2>num3 and num2>num1:
    print(num2, "num2 is biggest")
else:
    print("num3 is biggest")
'''

#weekday
choice = int(input("enter a number between 1 to 7: "))
match choice:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
    case _:
        print("invalid input")
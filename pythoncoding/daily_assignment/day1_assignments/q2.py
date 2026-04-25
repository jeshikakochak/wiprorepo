#check leap year or not
year=int(input("enter a year "))
if year%400==0 or year%4==0 and year%100!=0:
    print("it is a leap year")
else:
    print("it isnt a leap year")
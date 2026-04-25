#count vowels in a string
text= input("enter a string")
count=0
for i in text:
    if i in "aeiou ":
        count+=1
print("number of vowels= ",count)
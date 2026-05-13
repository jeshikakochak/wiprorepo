# nat nos print

'''num=int(input('Enter the number'))
value=1

while(value<=num):
    print(value)
    value+=1'''

num = input('Enter a number: ')
count = len(num)
ni = int(num)
comp = ni
sum = 0
while ni > 0:
    rem = ni % 10
    sum += rem ** count
    ni = ni // 10
if comp == sum:
    print('Arm')
else:
    print('NA')
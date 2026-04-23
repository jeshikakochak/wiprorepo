#create a list with 5 different types of fruits. print the list
list=['apple','banana','guava','orange','grapes']
print(list)

#add two more fruits to the list, then remove one fruit from it.print the updated list
list.append("mango")
list.append("pineapple")
list.remove("apple")
print(list)

#access the second and fourth fruits in the list.print them
print(list[1])
print(list[3])

#slice first three fruits
print(list[0:3])

#find length of list
print(len(list))
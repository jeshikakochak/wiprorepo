#create a set of 5 unique colors.print the set
color={"red","blue","green","yellow","black"}
print(color)

#add a new color to the set, then try removing an existing color.print the updated set
color.add("white")
color.remove("black")
print(color)

#create another set with 3 different colors find the intersection,union,and difference between both sets
colors={"blue","pink","green"}
print(color.intersection(colors))
print(color.union(colors))
print(color.difference(colors))

#check if a specific color is in the set and print the result
print('blue' in color)

#convert a list of fruits(with some suplicates)into a set and print the unique fruits
fruits=["apple","mango","apple","banana","mango"]
unique_fruits=set(fruits)
print(unique_fruits)
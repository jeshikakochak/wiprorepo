#create a dictionary with your name,age,favorite hobby as keys,and provide appropriate values.print the dictionary
student={"name":"jeshika", "age":22 , "hobby":"dancing"}

print(student)

#access and print the value associated with your name in the dictionary
print(student["name"])

#add a new key-value pair for your favorite food, then update the value for your favorite hobby.print the updated dictionary
student["favorite food"]="pizza"
student["hobby"]="reading"
print(student)

#print all the keys and all the values in the dictionary separately
print(student.keys())
print(student.values())

#remove the age key-value pair from the dictionary.print the dictionary to see the change
student.pop("age")
print(student)
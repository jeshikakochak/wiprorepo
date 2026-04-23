#create a tuple with the names of 3 different cities you'd like to visit.print the tuple.
city=("delhi","bhopal","indore")
print(city)

#access and print the first and last elements of the tuple
print(city[0])
print(city[-1])

#create another tuple with 2 more cities. concatenate both tuples and print the result
city_plus=("goa","chennai")
all_city=city+city_plus
print(all_city)

#try changing one element of the tuple what haappens?
#city[0]="pune"
#print(city)
#tuple is immutable

#unpack the elements of the tuple into separate variables and print them
city1,city2,city3=city
print(city1,city2,city3)
import os
import csv
'''
empid, ename
101, AAA
102, BBB'''

def write_csv(file_name):
    data:[
        {"name":"poornima","age":30},
        {"name":"raju","age":25}
    ]
    columnnames=["name","age"]
    with open(file_name,"w",newline='\n') as file:
        writer= csv.DictWriter(file,fieldnames=columnnames)
        writer.writerheader()
        writer.writerows(data)

def read_csv(file_name):
    with open(file_name,"r",newline="\n") as file:
        reader=csv.DictReader(file)
        for row in reader:
            print(f"name: {row["name"]},age={row["age"]}")

def delete_csv(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"{file_name} deleted successfully")
    else:
        print(f"{file_name} does not exists")

file_name="myfile.csv"
write_csv(file_name)
print("data read from csv file:")
read_csv(file_name)
delete_csv(file_name)

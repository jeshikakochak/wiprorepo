filename=input("enter file name:")
try:
    f=open(filename,"r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("file not found")
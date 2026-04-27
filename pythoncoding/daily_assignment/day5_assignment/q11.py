try:
    f=open(input("enter file name: "),"r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("file not found!")
finally:
    print("program completed")
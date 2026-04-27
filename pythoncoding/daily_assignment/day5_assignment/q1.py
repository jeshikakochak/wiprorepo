#write text to a file and read it back
text=input("enter some text:")
f=open("output.txt","w")
f.write(text)
f.close()
f=open("output.txt","r")
print(f.read())
f.close()
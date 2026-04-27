import re
'''txt=input("enter a text ") #india is my country
bpat=input("enter beginning pattern ") #india
epat=input("enter ending pattern ") #country
bpat='^'+bpat  #^india
epat=epat+'$' #try$

if re.search(pattern=bpat,string=txt):
    print("beginning pat available")
else:
    print("ending pat not available")'''

'''#digit
mbno=input("enter a text")
pat="[0-9]"
if re.search(pattern=pat,string=mbno):
    print("only digits")
else:
    print("other chars available")'''

'''#digit   
mbno=input("enter a text")
pat=r"\d"
if re.fullmatch(pattern=pat,string=mbno):
    print("only digits")
else:
    print("other chars available")'''


'''#username
un=input("enter un")
pat=r"^[a-z]{8}$"
if re.match(pattern=pat,string=un):
    print("valid")
else:
    print("invalid")'''

'''#email
emailadd=input("email")
pat=r"^[a-zA-Z0-9_]+@[a-z]+\.[a-z]+$"
if re.match(pattern=pat,string=emailadd):
    print("valid")
else:
    print("invalid")'''

'''#pwd
pwdtxt=input("pwd: ")
pat=r"^(?=.*[A-Z])(?=[a-z])(?=.*[0-9])(?=[@_-]){8,}$"
if re.match(pattern=pat,string=pwdtxt):
    print("valid")
else:
    print("invalid")'''

txt=input("text")
pat=r"\s+"
print(re.sub(pattern=pat,string=txt,repl='*'))
print(re.split(pattern=pat,string=txt))

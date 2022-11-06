import json
# import re
# import os
from aifc import open
from builtins import input, print
def fun():
    fn=[]
    ln=[]
    un=[]
    pn=[]
    pw=[]
    conformp=[]
    b={}
    c=[]
    fn.append(input("Enter first name:"))
    ln.append(input("choose your second name:"))
    un.append(fn+ln)
    pn.append(input("enter phone number"))
    pw.append(input("choose your password:"))
    conformp.append(input("Enter conform password as password"))
    if pw==conformp:
        print("Your signup is succesfully completed")
        b["FirstName"]=fn
        b["LastName"]=ln
        b["user Name"]=un
        b["PhoneNo"]=pn
        b["Password"]=pw
        b["Comformpw"]=conformp
        # b={"firstname":fn,"lastname":ln,"pnonenumber":pn,"password":pw,"conformpa":conformp}
        c.append([b])
        with open("pavigopal.json","w")as f:
            json.dump(b,f,indent=3)
        # return sn
    else:
        print("password is wrong")
def login(un,passwords):
    un=[]
    passwords=[]
    password=""
    username=""
    un=input("Enter your username:")
    password=input("Enter your Password:")
    if password==passwords:#[un.index(username)]:
       print("welcome")
    else:
       print("incorrect!")

a=""
while True:
    a=input("enter signup login")
    if a=="signup":
       fun()
    if a=="login":
       password=""
       username=""
       usernames=[]
       passwords=[]
       login(usernames,passwords)
    # if a=="c":
    break
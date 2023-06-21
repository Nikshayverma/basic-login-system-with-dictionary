import random
import string
def randompass():
    passwrd=''
    alphanum=("abcdefghijklmnopqrstuvwxyz0123456789!@#$")
    for i in range (6):
        passwrd+=''.join(random.choice(alphanum))
    print("------------------------\n"
          "your password is :  ",passwrd ,"\n")
    return passwrd

loginids={1:'123',2:'123'}
def add_login():

    login_id = int(input("create login id"))
    password=int(input(" enter 1 to create a password or \n enter 2 to create a random password"))
    if password==2:
        password=randompass()
    elif password==1:
        password=str(input("create passsword using alpha numerics"))
    else:
        print("wrong choice   \n Add login")
        add_login()
    print("ID Created Successfully ")
    user_input=input("want to create more ids ? yes/no  ")
    user_input=user_input.lower()
    if user_input=="yes":
        loginids[login_id]=password
        add_login()
    elif user_input=="no":
        print("not adding")
        loginids[login_id]=password

def update_login():
    login_id = int(input("enter login id  to update"))
    if login_id not in loginids.keys():
        print("wrong login id")
        
    else:
        new_password=str(input("enter new password : "))
        loginids[login_id]=new_password
        print("Successfully Updated")


def login():
    enter_login=int(input("enter login id : "))
    if enter_login not in loginids.keys():
        print("wrong login id")
        
    else:
        enter_password=str(input("enter password : "))
        if loginids[enter_login]==enter_password:
            print("Welcome")
            return 0
        else:
            print("wrong password")
            return 1

def remove_login():
    login_id = int(input("enter login id  to remove"))
    if login_id not in loginids.keys():
        print("wrong login id")
        
    else:
        loginids.pop(login_id,"error")
        print("Successfully Removed")
        
def showlogin():
    print("login ids are:  ")
    for i in loginids:
        print (i,":" , loginids[i] )




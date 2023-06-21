import loginsystem

def mainmenu():
    inpt=int(input("enter 1 to add login id  \n"
          "enter 2 to remove login id  \n"
          "enter 3 to update password \n"
          "enter 4 to show current login id's \n"
          "enter 5 to login again \n"
          "enter 6 to quit :    \n"
          "---------------------- \n"))
    if inpt==1:
        loginsystem.add_login()
        
    elif inpt==2:
        loginsystem.remove_login()
    
    elif inpt==3:
        loginsystem.update_login()
        
    elif inpt==4:
        loginsystem.showlogin()
        
    elif inpt==5:
        loginn()

    while inpt!=6:
        mainmenu()

def loginn():
    output= loginsystem.login()
    if output==0:
        mainmenu()
    else:
        print("wrong login")          

loginn()
users = {}

def register():
    username = input("Username: ")
    password = input("Password: ")
   
    
    users[username] = password 





def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")


    if username in users:
        if  users[username] == password:
            print( f"Welcome {username}")
        else:
            print("Invalid username")
    else:
      print("Invalid password")  

register()      
login()


current user = None

def profile():
    print("This is your private profile")

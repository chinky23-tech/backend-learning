users = {}
current_user = None


def login_required(func):
    def wrapper(*args, **kwargs):
        if current_user is not  None:
            return func(*args, **kwargs)
        else:
            print("login first")
    return wrapper           
def register():
    username = input("Username: ")
    password = input("Password: ")
   
    
    users[username] = password 





def login():
    global current_user
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

@login_required

def profile():
    print("This is your private profile")
profile()
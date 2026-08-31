#task 1
"""
def greet_user():
     print("hello")
count = 0

while count < 3: 
   greet_user()
 
   count = count + 1
"""
#task 2
"""
def ask_name(name):
    
    print("hello" + name)

while True:
   name = input("enter your name: ")
   if name == "quit":  
       break
   else:
       ask_name(name)
       """
#task 3

def greet(name):
    print("hello" + " " + name)
while True:
    name = input("Enter name:")
    if  name == "quit":
        break
    if name == "admin":
        continue
    else:
        greet(name)

    
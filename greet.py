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
"""
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
"""
    #task 4
products = {"pencil" : 30,"pen" :50,"copy" : 20}
cart = []
def check_product():
  
        while True:
            product = input("Enter product :")
            
            if product == "quit":
                
                break   
            
            if product not in products:
              
            
              continue 
            
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("quantity must be greater than 0")
                print("please enter a valid quantity")
                continue
            cart.append([product, quantity, products[product]])
check_product()
total = 0
for product_name , quantity, price in cart:
    print(product_name, quantity, price)  
    total += quantity * price 

print("total is ", total)

                
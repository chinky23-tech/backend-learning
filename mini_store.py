#def calculate_total(price1, price2, price3):
    #return price1 + price2 + price3


#total = calculate_total(100 , 200 , 200)
#print(total)

#product = {"laptop" : "50000", "keyboard" : "20000"}
#def show_products(product):

 #for product_name, price in product.items():
   #print(product_name, price)

#show_products(product)

#Task 1
products = {"laptop" : "50000" , "phone": "30000" , "tablet": "20000" , "keyboard": "2000"}
def show_products(products):


   for product_name, price in products.items():
        print(product_name, price) 
show_products(products)    

#Task 2
def get_price(products, products_name):
    return products.get(products_name)
    products_name = products.get(products_name) 
    

    
   

#Task 3
"""
def calculate_total(price1, price2, price3):
    return price1 + price2 + price3 

for  product_name , price in products.items():
    print(price)

#Task 4

def buy_product(products, products_name):
    if products in products:
        print("display its price")
    else:
        print("product is not available")    

    buy_product(products)   
"""

# task 5

def greet_user(chinky):
   
   return "hello"  + " " + chinky

result = greet_user("chinky")
print(result)
#task 6

def double_number(number):
    return number + number
result = double_number(10)
print(result)

#task 7

price = 1000
discount = 10
def calculate_discount(price, discount ):
    return price * discount / 100
result = calculate_discount(price,discount)
final_price = price - result
print(result)
print(final_price)

#task 8 
price = 1000

def check_discount(price):
    if price >= 1000:
         return "10% discount available"
    else:
        return "no discount" 
message = check_discount(price)
print(message)

#task 9 
products = {"laptop" : "50000" , "phone" : "30000" , "tablet" : "20000" , "keyboard" : "2000"}
product_name = "laptop"
def check_product(products, product_name):
    if product_name in products:
     
        return "its price "  + " : " + products[product_name] 
    else:
        return "product is  not available"
message = check_product(products, product_name )
print(message)    
#task 10

def buy_product(products, product_name):
    if product_name in products:
        return "You bought" + " " + (product_name) + ", " + " price " + products[product_name]  
    else:
        return "Product not avialabe"
message = buy_product(products, product_name)
print(message)    

#task 11
products = {"laptop": 50000, "keyboard": 2000, "phone": 30000}
cart = ["laptop", "keyboard", "phone"]

def calculate_cart_total(products, cart):
    total = 0 
    for product_name in cart:
      
        total += products[product_name]
    return total 


cart_total = calculate_cart_total(products, cart)
print(cart_total) 

#task12
numbers = [10, 20, 20, 40]

def calculate_sum(numbers):
    total = 0
    for  number in numbers:

     total += calculate_sum(number)
    return(total)
    print(numbers)

    #task13
products = {"laptop" : 50000 , "phone" : 30000 , "tablet" : 20000 , "keyboard" : 2000}

    
def add_products(products):

  list = []
   
for product_name, price in products.items():
   
    if price >= 10000:
       
      list.append(product_name)

     


result = list(products)
print(result)

    



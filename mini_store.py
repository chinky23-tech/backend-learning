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
"""
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


     


result = list(products)
print(result)
"""
#task 13

"""
age = int(input("enter your age : "))
age = age+10
print("in 10 years you will be" ,    age)
"""
    


#task 14
"""
def calculate_future_age(age):
     return age + 10
age = int(input("enter your age :")) 


result = calculate_future_age(age)
print("your age will be" , result , "after ten years")
"""

#task  15
"""
products = ["top"]
def product_availabe():
 product =    input("enter product name")
 
 if product in products:
      return "product available"
 else:
    return "product not available"
result = product_availabe()
print(result)
"""
     
    #task 16


"""
products = {"top": 1000, "jeans": 2000, "dress": 3000} 

def check_product():
   product = input("enter product name :")
   if product in products:
     return products[product]
   else:
     return "not available"   
result = check_product()
print(result)
"""
    #task 17

products = {"socks" : 100, "pen": 20 , "pencil": 30}
cart = []
def new_product():
 product = input("Enter product name: ")
 
 if product in products:
  cart.append(product)
  return product
 else:
  return "not available"
 

result = new_product()

print(cart,result)


 
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




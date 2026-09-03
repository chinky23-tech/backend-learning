#task 1

products = {"pencil": 30, "pen": 20, "copy": 40}
cart = []
number_words = {"one" : 1, "two" : 2, "three": 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9, "ten" : 10} 

def check_product(product):

    if product in products:
        return products[product]
    else:
        return "product not available"


while True:

    product = input("Enter product (or quit): ")
    
    if product == "quit":
        break

    result = check_product(product)

    if result == "product not available":
        print(result)
        continue

    quantity_input = input("Enter quantity: ").lower()

    try:
       quantity = int(quantity_input)

    except ValueError:
        if quantity_input in number_words:
            quantity = number_words[quantity_input]

        else:
         print("please enter a valid number")
         continue
    
    if quantity <= 0:
        print("quantity must be greater than 0")
        continue

    total_price = result * quantity

    cart.append([product, quantity, result])

    print(f"{product} : {quantity} x {result} = {total_price}")


print("Cart:", cart)

def calculate_total(cart):
 total = 0
 for product_name, quantity , price in cart:
   total += quantity * price 
 return total


def print_bill(Cart):

   for product_name, quantity, price in cart:
      print(f"{product_name} : {quantity} x {price} = {quantity * price}")

total = calculate_total(cart)
print_bill(cart)
print(f"Total is : {total}")


products = ["laptop" , "phone" , "tablet" , "keyboard"]

print("=== MINI STORE ===")

print("Avialable products:")

print(products)

product = input("Enter product you want")

if product in products:
    print("product is avialable")
else:
    print("product is not avialable")    
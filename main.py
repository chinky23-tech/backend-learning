price = 50000

quantity = 2

cart_total = price * quantity

if cart_total >= 50000:
    discount = 20
elif cart_total >= 20000:
     discount = 10
else:
     discount = 0

discount_amount = cart_total * discount / 100

final_price = cart_total - discount_amount

print("Cart Total:", cart_total)

print("Discount:" , discount, "%")

print("Discount amount:", discount_amount)

print("final_price:", final_price)
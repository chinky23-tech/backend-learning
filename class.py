class Product:
    def __init__(self, name, price,num):
        self.name = name
        self.price = price
        self.num = num

    def show_product(self):
        print(self.name, self.price,self.num) 

    def total_value(self):
       return self.price * self.num
     

    def update_price(self, new_price):

        if new_price >= 0:
            self.price = new_price
        else:
            print("Price must be greater than 0")    



laptop = Product("Laptop", 5000,5) 
phone = Product("Phone", 30000, 2)
keyboard = Product("Keyboard" ,2000, 10 )

phone.update_price(32000)
print(phone.price)
phone.update_price(-5000)
print(phone.price)
print(laptop.total_value()) 
print(phone.total_value())
print(keyboard.total_value())

    
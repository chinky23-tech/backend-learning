class Product:
    def __init__(self, name, price,num):
        self.name = name
        self.price = price
        self.num = num

    def show_product(self):
        print(self.name, self.price,self.num) 

    def total_value(self):
       return self.price * self.num
     
    

laptop = Product("Laptop", 5000,5) 
phone = Product("Phone", 30000, 5)
keyboard = Product("Keyboard" ,2000, 10 )



print(laptop.total_value()) 
print(phone.total_value())
print(keyboard.total_value())

    
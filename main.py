def say_hi():
 print("Hi")
def my_decorator(func):
 print("Before function")
 func()
 print("After function")
my_decorator(say_hi)

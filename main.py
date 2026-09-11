def login_required(func):
    @login_required
    def view_profile():
     print("showing profile")
def wrapper():  
   logged_in = True

   if logged_in:
       func()
   else:
      print("please login first")      
      return wrapper
#task 1

user = {"name" : "chinky" , "age" : 35 , "city" : "Patiala"}
user["city"] = "chandigrah"
user["skill"] = "python"
user["email"] = "example@gmail.com"

for key , value in user.items():
    print(key, ":" ,value)

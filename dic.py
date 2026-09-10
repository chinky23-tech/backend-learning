#task 1
"""
user = {"name" : "chinky" , "age" : 35 , "city" : "Patiala"}
user["city"] = "chandigrah"
user["skill"] = "python"
user["email"] = "example@gmail.com"

for key , value in user.items():
    print(key, ":" ,value)
if "phone" in user:
    print("phone exist")
else:
    print("phone not found")    
    """
#task2 
users = {
    "user1" : { 
        "name" : "chinky",
        "age" : 35,
        "skill" : ["python" , "react"],

    },
    "user2" : {
        "name" : "rahul",
        "age" : 26,
        "skill" : ["node.js" , "express.js"]

    }
}
user_skill_input  = input("Enter your skill:")

for user_id , user_data in users.items():
     for user_skill in user_data["skill"]:
      if user_skill == user_skill_input:
       print(f"{user_data["name"]} knows {user_skill_input}")
    
    
    

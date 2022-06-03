import admin as tt

class User:
    login_info = {"Barkha": "bar2008@"}

    
    def __init__(self, name, no, email, add, passw):
        self.name = name
        self.no = no
        self.email = email
        self.add = add
        self.passw= passw
        User.login_info[self.name] = self.passw
        self.order_history = {}
        self.user_info = {}
    
        
    @classmethod
    def login(cls, username, password):
        if cls.login_info.get(username) == password:
            return True
        else:
            print("SORRY! These are the Wrong Credentials")
            return False
        

    
    def add_new_user(self):
        
       profile= {}
       
       name = input("Enter the  name: ")
       uid = int(input("Enter the user  id: "))
       no = int(input("Enter the no: "))
       email =(input("Enter the email: "))
       add = (input("Enter the address: "))
       passw = (input("Enter the password: "))
       profile[uid] = {
            "UserName": name,
            "Userid": uid,
            "Phoneno": no,
            "EmailId": email,
            "Address": add,
            "Password": passw
        }
       print(profile)
       print("The user "+name+ "is successfully added")
       User.login_info[name] = passw
       self.user_info[uid] = {
                    "user Name": profile[uid]["UserName"],
                    "EmailId": profile[uid]["EmailId"],
                    "Phoneno": profile[uid]["Phoneno"],
                    "Address": profile[uid]["Address"],
                    "Passsword": profile[uid]["Password"],
                    }
    def edit_profile(self):
        profile = {}
        uid = int(input("Enter the user id which you want to edit: "))
        Name = input("Enter the user name")
        no = int(input("Enter the phoneno. of user")) 
        email = input("Enter the email id of the user")
        add = (input("Enter the Address of the user"))
        passw= (input("Enter the password"))
        profile[uid] = { "UserName": Name, "Userid": uid,"Phoneno": no, "EmailId": email, "Address": add,"Password": passw}
        print(profile)
        print("****Profile updated successfully*****")
        return True
       

    def place_order(self):
        print("What you want to order.... Here is the Menu")
        print(tt.show_menu())
        user_choice = int(input("If you want to order then select 1.YES 2.NO"))
        if user_choice == 1:
            n= int(input("Enter how many items do you want to Order"))
            x=0
            for i in range(n):
             
             Foodid = int(input("Enter the Item id here: "))
             quan = int(input("Enter the quantity of the item: "))
             x += (tt.menu[Foodid]["Price"] * quan)*(100-tt.menu[Foodid]["Discount"])/100
            again_ask = input("Are you still want to order this Enter YES or NO")
            if again_ask == "YES":
                print(f'''Your item name is {tt.menu[Foodid]["FoodName"]}''')
                print(f'''Price of your Item is {tt.menu[Foodid]["Price"]}''')
                print(f"This is your quantity {quan}")
                print(f"It costs you {x}INR in total")
                print("You're all set for this order")
                self.order_history[Foodid] = {
                    "Food  Name": tt.menu[Foodid]["FoodName"],
                    "Price": tt.menu[Foodid]["Price"],
                    "Quantity": quan
                }
                final_stock = tt.menu[Foodid]["Stock"] - quan
                tt.menu[Foodid]["Stock"] = final_stock
                print("You're order is successfully placed")

            elif again_ask == "NO":
                print("This Order is cancelled!! You can look once more")
            else:
                print("Invalid choice")
        elif user_choice == 2:
            print("You select 2 option so we cancelled this")
        else:
            print("Enter the invalid choice")

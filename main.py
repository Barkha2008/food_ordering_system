import admin as aa
import user as us
from user import User

uhh = User(str, str, str, str, str)

inp = int(input("Welcome to SAMRAT RETUARANT: 1.Admin and 2.User and 3.Registration 4.Exit"))
if inp == 1:
    Username = input("Enter the username of admin: ")
    Password = input("Enter the password of admin: ")
    if aa.admin_keys[Username] == Password:
        print("*****You're successfully logged inn*****")
        admin_crawler = True
        while admin_crawler:
            adm_choice = int(input("Choose the options of admin panel 1.ADD NEW ITEM 2.EDIT ITEM 3.VIEW MENU 4.REMOVE ITEM 5.EXIT"))
            if adm_choice == 1:
                aa.add_new_item()
            elif adm_choice == 2:
                aa.edit_profile()
            elif adm_choice == 3:
                aa.show_item()
            elif adm_choice == 4:
                aa.remove_item()
            elif adm_choice == 5:
                print(f"You're Exit to the admin panel{Username}")
                admin_crawler = False
            else:
                print("This is the wrong selection please select valid option")
    else:
        print("These are the wrong credentials! SORRY!!!")
elif inp == 2:
    print("Welcome to the user panel")
    username = input("Enter the username here: ")
    password = input("Enter the password here: ")
    if User.login(username, password):
        print(f"You are logged in successfully {username}")
        user_crawler = True
        while user_crawler:
            usr_choice = int(input(f"{username}, Enter the option 1.Place new order 2.Order history  3.Profile 4.Edit Profile 5.Exit"))
            if usr_choice == 1:
               uhh.place_order()
            elif usr_choice == 2:
                 print(f"Here is your order history, {username}")
                 print(uhh.order_history)
            elif usr_choice == 3:
                 print(f"Here is user information, {username}")
                 print(uhh.user_info)
            elif usr_choice == 4:
                 uhh.edit_profile()     
            elif usr_choice == 5:
                 user_crawler = False
                 print("You're Successfully looged out")
            else:
                  print("You choose the invalid option")
    else:
         print("These are the wrong credentials! SORRY!!!")
elif inp == 3: 
    uhh.add_new_user()
    inp = int(input("WELCOME TO SAMRAT RETUARANT 1.Admin and 2.User and 3.egistration 4.Exit"))
if inp == 1:
    Username = input("Enter the username of admin: ")
    Password = input("Enter the password of admin: ")
    if aa.admin_keys[Username] == Password:
        print("*****You're successfully logged inn*****")
        admin_crawler = True
        while admin_crawler:
            adm_choice = int(input("Choose the options of admin panel 1.ADD NEW ITEM 2.EDIT ITEM 3.VIEW INVENTORY 4.REMOVE ITEM 5.EXIT"))
            if adm_choice == 1:
                aa.add_new_item()
            elif adm_choice == 2:
                aa.edit_from_item()
            elif adm_choice == 3:
                aa.show_menu()
            elif adm_choice == 4:
                aa.remove_item()
            elif adm_choice == 5:
                print(f"You're Exit to the admin panel{Username}")
                admin_crawler = False
            else:
                print("This is the wrong selection please select valid option")
    else:
        print("These are the wrong credentials! SORRY!!!")
elif inp == 2:
    print("Welcome to the user panel")
    username = input("Enter the username here: ")
    password = input("Enter the password here: ")
    if User.login(username, password):
        print(f"You are logged in successfully {username}")
        user_crawler = True
        while user_crawler:
            usr_choice = int(input(f"{username}, Enter the option 1.Place new order 2.Order history 3.Profile 4.Edit Profile 5.Exit"))
            if usr_choice == 1:
               uhh.place_order()
            elif usr_choice == 2:
                 print(f"Here is your order history, {username}")
                 print(uhh.order_history)
            elif usr_choice == 3:
                 print(f"Here is user information, {username}")
                 print(uhh.user_info)
            elif usr_choice == 4:
               uhh.edit_profile()     
            elif usr_choice == 5:
                 user_crawler = False
                 print("You're Successfully looged out")
            else:
                  print("You choose the invalid option")
    else:
         print("These are the wrong credentials! SORRY!!!")

    
else:
    Exit()
    





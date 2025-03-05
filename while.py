

# username = input("Enter your username: ")
# password = input("Enter your password: ")

# print("\nNow you need to enter your username and password again...\n")

# while True:
#     check_user = input("Enter your username: ")
#     check_pass = input("Enter your password: ")

#     if check_user == username and check_pass == password:
#         print(f"Login successful welcome {username}")
#         break  
#     else:
#         print(" Incorrect username or password! Please try again.")


import getpass

username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")  

print("\nNow you need to enter your username and password again...\n")

while True:
    check_user = input("Enter your username: ")
    check_pass = getpass.getpass("Enter your password: ")

    if check_user == username and check_pass == password:
        print("Login successful!")
        break
    else:
        print(" Incorrect username or password! Please try again.")








# userName_2 = input("Enter your username: ")


# password = input("Enter your password: ")


# while password != "4280":
#     print("password is wrong")
#     password = input("Enter your password: ")

# print(f"welcome {userName_2}")


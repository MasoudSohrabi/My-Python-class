print("Hello , Please enter your first and last Name:")

firstName = input()
lastName = input()

print(f"welcome {firstName} {lastName}, to continue. ")

nextStep = input("Press enter")


print("Please enter your Age: \n(Warning: Only +18 can access to data!)")

userAge = input()


if userAge >= 18:
    print("You can access to data")
elif userAge < 18:
    print("You can not access to data")    


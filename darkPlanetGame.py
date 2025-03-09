print("Welcome to Dark Planet \nYou are a passenger from Earth!\n")

userName = input("Please enter your username:")
print(f"Hi {userName} , We'll hope you enjoy the adventure!\n")

print("-------------------------------------\n")

print("You are now standing on the accursed hills of the Dark Planet!\n")
print("What path will you choose to continue?\n")

level_1_select1 = "Mountain"
level_1_select2 = "Forest"
userSelect_L1 = input("M(Mountain) or F(Forest): ").upper()


if userSelect_L1 == "M":
    print("You choose Mountain! A hard and cold path!\n")
    print("-------------------------------------\n")
    print("Do you want to continue?\n")
    userSelect_M_continue1 = input("Yes or No: \n").lower()
    print("-------------------------------------\n")
    if userSelect_M_continue1 == "yes":
        print("You are in Mountain now! Keep calm and Becareful.")
        print("-------------------------------------\n")
        print("Here is a sword in the stone.\nYou need this sword to continue your journey.\nBut to get it, you have to solve a riddle.\n")
        print("-------------------------------------\n")
        print("What moves all the time but never leaves its place?\n")
        
        
        riddle_1_answer = input("Answer: \n").lower()
        if riddle_1_answer == "clock":
            print("Correct! you've got the Arthur's sword!.")
        else:
            print("Wrong! you lose the Arthur's sword!.")   
            print("-------------------------------------\n")
        print("Do you want to continue?\n")
        userSelect_M_continue2 = input("Yes or No: \n").lower()
        print("-------------------------------------\n")
        if userSelect_M_continue2 == "yes":
            print("We continue along the mountain path and reach a bridge.\n"
                "On this bridge there is a magical dragon that you must defeat to cross.\n"
                "Will you continue?\n")
            userSelect_M_continue3 = input("Yes or No: \n").lower()
            print("-------------------------------------\n")
            if userSelect_M_continue3 == "yes":
                    print("Well, brave one! To defeat this dragon,\n"
                    "you must strike a specific spot with your sword because this dragon is invincible \n"
                    "and has only one weak point. If you don't strike correctly, \n"
                    "you will be eaten by the dragon. \n"
                    "A tip: Remember the story of Achilles!")
                    print("-------------------------------------\n")
                    userAttack = input("where do you want to attack?").lower()
                    if userAttack == "heel":
                        print("Corrrectt! You got the dragon skin and the treasure the dragon was guarding, \n"
                        "YOU WON THIS GAME!")
                    else:
                        print("Wrong... You Died...")    
            else:
                    print(f"Okay. Goodbye {userName}")
        else:
                print(f"Okay. Goodbye {userName}")        
    else:
        print(f"Okay. Goodbye {userName}")
        print("-------------------------------------\n")
elif userSelect_L1 == "F":
    print("You choose Forest! A foggy and dark path path!\n") 
    print("-------------------------------------\n")
    print("Do you want to continue?\n") 
    userSelect_F_continue1 = input("Yes or No: \n").lower()
    print("-------------------------------------\n")
    if userSelect_F_continue1 == "yes":
        print("You are in Forest now! Do Not be afraid and stay quiet.")
        print("-------------------------------------\n")
    elif userSelect_F_continue1 == "no":
        print(f"Okay. Goodbye {userName}")
else: 
    print("Please enter a correct path!")    



print("-------------------------------------\n")



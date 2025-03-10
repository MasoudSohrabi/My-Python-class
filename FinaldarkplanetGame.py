print("Welcome to Dark Planet \nYou are a passenger from Earth!\n")

userName = input("Please enter your username:")
print(f"Hi {userName}, We hope you enjoy the adventure!\n")

print("-------------------------------------\n")

print("You are now standing on the accursed hills of the Dark Planet!\n")
print("What path will you choose to continue?\n")

while True:
    userSelect_L1 = input("M(Mountain) or F(Forest): ").upper()
    if userSelect_L1 in ["M", "F"]:
        break
    print("Invalid choice! Please enter 'M' for Mountain or 'F' for Forest.")

if userSelect_L1 == "M":
    print("You chose Mountain! A hard and cold path!\n")
    print("-------------------------------------\n")

    while True:
        userSelect_M_continue1 = input("Do you want to continue? (Yes or No): \n").lower()
        if userSelect_M_continue1 in ["yes", "no"]:
            break
        print("Invalid input! Please enter 'Yes' or 'No'.")

    if userSelect_M_continue1 == "yes":
        print("You are in the Mountain now! Keep calm and Be careful.")
        print("-------------------------------------\n")

        print("Here is a sword in the stone. You need this sword to continue your journey.")
        print("But to get it, you have to solve a riddle.\n")
        print("-------------------------------------\n")

        print("What moves all the time but never leaves its place?\n")

        has_sword = False  # متغیر بررسی داشتن شمشیر
        attempts = 3
        while attempts > 0:
            riddle_1_answer = input("Answer: \n").lower()
            if riddle_1_answer == "clock":
                print("Correct! You've got the Arthur's sword!")
                has_sword = True
                break
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"Wrong! You have {attempts} attempts left.")
                else:
                    print("Wrong! You lost the Arthur's sword!")

        if not has_sword:
            print("You cannot continue without the sword! Game Over.")
            exit()

        print("-------------------------------------\n")
        userSelect_M_continue2 = input("Do you want to continue? (Yes or No): \n").lower()

        if userSelect_M_continue2 == "yes":
            print("We continue along the mountain path and reach a bridge.")
            print("On this bridge, there is a magical dragon that you must defeat to cross.")
            print("Will you continue?\n")

            userSelect_M_continue3 = input("Yes or No: \n").lower()

            if userSelect_M_continue3 == "yes":
                print("Well, brave one! To defeat this dragon, you must strike a specific spot with your sword.")
                print("A tip: Remember the story of Achilles!")

                attempts = 2  # دو فرصت برای شکست دادن اژدها
                while attempts > 0:
                    userAttack = input("Where do you want to attack? ").lower()
                    if userAttack == "heel":
                        print("Correct! You got the dragon skin and the treasure the dragon was guarding!")
                        print("YOU WON THIS GAME!")
                        break
                    else:
                        attempts -= 1
                        if attempts > 0:
                            print(f"Wrong! You have {attempts} attempt left.")
                        else:
                            print("Wrong... You Died...")

elif userSelect_L1 == "F":
    print("You chose Forest! A foggy and dark path!\n")
    print("-------------------------------------\n")

    while True:
        userSelect_F_continue1 = input("Do you want to continue? (Yes or No): \n").lower()
        if userSelect_F_continue1 in ["yes", "no"]:
            break
        print("Invalid input! Please enter 'Yes' or 'No'.")

    if userSelect_F_continue1 == "yes":
        print("You are in the Forest now! Do not be afraid and stay quiet.")
        print("-------------------------------------\n")

        print("Here is a magic wood in that tree.")
        print("You need this magic wood to continue your journey.")
        print("But to get it, you have to solve a riddle.\n")
        print("-------------------------------------\n")

        print("What has lots of holes but still holds water?\n")

        has_magic_wood = False  # متغیر بررسی داشتن چوب جادویی
        attempts = 3
        while attempts > 0:
            riddle_2_answer = input("Answer: \n").lower()
            if riddle_2_answer == "sponge":
                print("Correct! You've got the Magic Wood!")
                has_magic_wood = True
                break
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"Wrong! You have {attempts} attempts left.")
                else:
                    print("Wrong! You lost the Magic Wood!")

        if not has_magic_wood:
            print("You cannot continue without the magic wood! Game Over.")
            exit()

        print("-------------------------------------\n")
        userSelect_F_continue2 = input("Do you want to continue? (Yes or No): \n").lower()

        if userSelect_F_continue2 == "yes":
            print("As we ventured deeper into the dark forest, we arrived at a cave.")
            print("The ultimate treasure of the game is hidden inside.")
            print("But to claim it, you must face a giant serpent that fiercely guards it.")
            print("Do you dare to continue?")

            userSelect_F_continue3 = input("Yes or No: \n").lower()

            if userSelect_F_continue3 == "yes":
                print("Alright, brave hero! This legendary serpent is highly sensitive to heat.")
                print("-------------------------------------\n")

                attempts = 2  # دو فرصت برای شکست دادن مار
                while attempts > 0:
                    userAttack1 = input("How do you want to attack? ").lower()
                    if userAttack1 in ["fire magic", "fire"]:
                        print("Correct! You have defeated the mighty serpent!")
                        print("You claimed one of its deadly fangs as a trophy, a symbol of your victory.")
                        print("Now, the treasure is yours, and you have conquered the game!")
                        print("YOU ARE THE ULTIMATE CHAMPION!")
                        break
                    else:
                        attempts -= 1
                        if attempts > 0:
                            print(f"Wrong! You have {attempts} attempt left.")
                        else:
                            print("Wrong... You Died...")

            else:
                print(f"Okay. Goodbye {userName}")

    else:
        print(f"Okay. Goodbye {userName}")

else:
    print("Please enter a correct path!")

print("-------------------------------------\n")

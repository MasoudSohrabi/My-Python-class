print("Enter your Name and Family name please:")


userName = input()
userFamily = input()

print("How old are you?") 

userAge = input()

print("Your data has been saved. \nIf you want to answer the questions \nenter Yes or if you don't want enter No")

userSelect = input()

userSelect = userSelect.lower()


if userSelect == "yes":
    print("Welcome " + userName + " " + userFamily)
    input("To continue press Enter")
    print("----------------------------------")

   
    print("Q1: How do you behave in social gatherings?\n A) Energetic and outgoing (Extrovert)\n B) Quiet and reserved (Introvert)")
    q1 = input("Your answer (A/B): ").upper()
    print("----------------------------------")

    
    print("Q2: How do you make decisions?\n A) Based on logic and analysis (Thinker)\n B) Based on feelings and intuition (Feeler)")
    q2 = input("Your answer (A/B): ").upper()
    print("----------------------------------")

    
    print("Q3: How do you approach tasks?\n A) With careful planning and organization (Planner)\n B) Flexible and spontaneous (Go-with-the-flow)")
    q3 = input("Your answer (A/B): ").upper()
    print("----------------------------------")

    
    if q1 == "A" and q2 == "A" and q3 == "A":
        print(" You are a Logical Leader!")
    elif q1 == "B" and q2 == "B" and q3 == "B":
        print(" You are an Emotional Artist!")
    elif q1 == "A" and q2 == "B" and q3 == "B":
        print(" You are a Social Creator!")
    elif q1 == "B" and q2 == "A" and q3 == "B":
        print(" You are a Creative Introvert!")
    else:
        print("🌟 Your personality is a unique mix of traits!")

elif userSelect == "no":
    print("Thanks for your attention, Bye.")

else:
    print("Invalid answer selected.")

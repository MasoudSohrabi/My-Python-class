import random

print("rock")
print("paper")
print("scissors")

randomMove = random.randint(0 , 2)

cpuMove = "paper"

if randomMove == 0:
    cpuMove = "rock"
elif randomMove == 1:
    cpuMove = "paper" 
elif randomMove == 2:
    cpuMove = "scissors"    
    
    


Player_1wins = 0
Player_2wins = 0
winningScore = 4
       
while Player_1wins < winningScore and Player_2wins < winningScore:
    print(f"player 1 : {Player_1wins} and player 2 : {Player_2wins}")
    Player_1 = input("Player_1 , make your move:").lower()
    print(f"Player_2 make your move: {cpuMove}")
    Player_2 = cpuMove

    if Player_1 == "q" or Player_1 == "quit":
        break

    if Player_1 == Player_2:
        print("draw!")
    elif Player_1 == "rock":
        if Player_2 =="scissors":
            print("Player_1 wins!")
            Player_1wins += 1
        elif Player_2 == "paper":
            print("Player_2 wins!") 
            Player_2wins += 1   
    elif Player_1 == "paper":
        if Player_2 == "rock":
            print("Player_1 wins!")
            Player_1wins += 1
        elif Player_2 == "scissors":
            print("Player_2 wins!")
            Player_2wins += 1
    elif Player_1 == "scissors":
        if Player_2 == "paper":
            print("Player_1 wins!")
            Player_1wins += 1
        elif Player_2 == "rock":
            print("Player_2 wins!")
            Player_2wins += 1
    else: 
        print("one of you input wrong option!")            

print(f"Final scores=> player1 : {Player_1wins} player2 :{Player_2wins} ")            
    
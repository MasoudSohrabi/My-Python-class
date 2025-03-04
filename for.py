# listNumber = [100 , 200 , 300 , 400 , 500]

# for num in listNumber:
#     print(num)


# numbers = range(1 , 9999 ,1000)    

# for num in numbers:
#     print(num)

for i in range(3):  
    num = int(input("Enter a number between 0 and 10: "))  

    if num == 7:
        print(" You have a golden number!")  
    elif 0 <= num <= 10:
        print(" Try again!")  
    else:
        print(" Out of range! Enter a number between 0 and 10.")  


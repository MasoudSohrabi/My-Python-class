# strings interpolation --> formatting string

userName = "masoud"
userFamily = "sohrabi"

result = f"username is {userName} userFamily is {userFamily}"

# print(result)


print("-----------------------")
#exercise
number_1 = 2
number_2 = 7
number_3 = 5
sum = f"sum is: {number_1 + number_2 + number_3} "
print(sum)
#or
person1 = "milad"
person2 = "maryam"
person3 = "mohammad"

question = f"my family name : \n {person1} my brother \n {person2} my mother \n {person3} my father "
print(question)







print("-----------------------")

#string indexes

# userName = "masoud" # masoud is a string ke tashkil shode az M , A , S , O , U , D 

#                                                            # 0   1   2   3   4   5

# NOW we want harfe 4ome masoud ro
print(userName[4]) # show---> u
print(userName[2]) # show---> s
print(userName[0]) #show---> m
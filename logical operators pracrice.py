# and , or , not

#Roller Coaster entering rules


#rules : under 130 cm - upper 210 cm - +18 age - under 60 age

visitorHeight = int(input("enter your Height:"))
visitorAge = int(input("enter your Age:"))


if (visitorHeight >= 130 and visitorHeight <= 210) and (visitorAge >= 18 and visitorAge <= 60 ) :
   print("You can enter to Roller coaster") 

elif not(visitorHeight >= 130 and visitorHeight <= 210) or (visitorAge >= 18 and visitorAge <= 60 ) :
   print("You can not enter to Roller coaster")



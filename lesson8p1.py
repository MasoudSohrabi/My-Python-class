# string

myName = "Masoud"    #or 'Masoud'
myFamily = 'Sohrabi'   #or "Sohrabi"

print(type(myName)) 
print(type(myFamily))
#both of them are 'str'

print('------------------------')
# for qout or naghle ghol
sentence = "masoud said : 'i am pro'"
print(sentence)
#or
sentence = 'masoud said : "i am pro"'
print(sentence)

print('------------------------')

#back slash \ 
#if we want to use ' ' in ' ' or bar ax 
sentence1 = 'masoud said : \'i am pro\' '
sentence2 = "masoud said : \"i am pro\" "
print(sentence1)
print(sentence2)

#backslash for new line ---> we use \n
sentence = " masoud is a boy \n he is 23"
print(sentence)

print('------------------------')

#if we want use the back slash in sentence --> we use \\
sentence = "masoud \\ sohrabi"
print(sentence)

print('------------------------')

#string concatenation -> (motasel kardan) 2 data poshte ham and beyneshoon space
myName = "masoud"
myFamily = "sohrabi"
#they are our data

#number1
myName = "masoud "
myFamily = "sohrabi"
print(myName + myFamily)

#number2
myName = "masoud"
myFamily = " sohrabi"
print(myName + myFamily)

#number3 
myName = "masoud"
myFamily = "sohrabi"
print(myName + " " + myFamily)

print('------------------------')

courseName = "Python"
# courseName = courseName + " course"    first way

#short hand for this:
courseName += " course"
print(courseName)

#for numbers

number = 3
print(number)

# number += 5
# print(number)

# number -= 2
# print(number)

# number *= 2
# print(number)

# number /= 3
# print(number)

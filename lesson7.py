#price of the product
from xml.sax.saxutils import prepare_input_source


waterPrice = 1000
print(type(waterPrice))
print(waterPrice)

print('----------------------------')

# Name of the product
waterName = "Damavand"
print(waterName)
print(type(waterName))
print('----------------------------')

# Is that available or not? / True or False / Yes or No
isthatavailable = True #or False
print(isthatavailable)
print(type(isthatavailable)) 
print('----------------------------')

#tags or "List" type
waterTag = ['water','Damavand']
print(waterTag)
print(type(waterTag))
print('----------------------------')

#dictionary type
water = {"waterPrice" : 1000 ,
         "waterName" : "Damavand"
 }
print(water)
print(type(water))
print('----------------------------')

#none type
personName = "Masoud"
personFamily = "Sohrabi"
personChild = None
print(personName , personFamily , personChild)
print(type(personChild))



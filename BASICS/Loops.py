#RANGE FUNCTIONS

def totalmarks():
    marks = [60,70,80]
    sum = 0
    for mark in marks:
     sum+=mark
    print(f" The total of the marks is:{sum}")
totalmarks()


#Range is afunction that takes the parameters of (start,stop,step)
#Examples   it works more like indexing , the stop number should be +1
#Using a loop,Print numbers from 0 to 6 (0,1,2,3,4,5,6)

   #0-5
for num in range(6):
   print(num)

   #0-10
for num in range(11):
   print(num)

   #1-20
def rangefrom1to20():
 for num in range(1,21):
   print(num)
rangefrom1to20()

#print the range of even numbers: from (2,4,6,8,10) #This prints odd numbers
def numbers():
  for num in range(2,11):
    if num % 2 != 0:
     print(num)
numbers()

def even_numb():
  for even in range(2,11,2):
    print(even)
even_numb()

#List and turples
#differences
#Lists are mutable and turples are not

#similarities
#they r all indexed

#syntax >list[]  , turples()

products = ['pen','pencil','book']
colors = ('red','green','pink')

#Qnts. 
# Add rubber to the product list
products.append('rubber')
print(products)
      
#add ruler to the product at the second position
products.insert(1,'ruler')
print(products)

#display the length of products
print(len(products))

#Turple
#Add purple to the turple of colors ,,,,Turples can not be editted
#so,  To edit a turple, convert it to a list and edit as below
new_colors = list(colors)
print(type(new_colors)) 
print(new_colors)

new_colors.append('purple')
print(new_colors)

# after performing a aprogram on it, convert the list back to  aturple
colors= tuple(new_colors)
print(colors)

fruits=('apple') # when  tuple has one item its a string so put a comma like 
fruits = ('apple',)
print(fruits, type(fruits))

#SETS 
# They are i mutable 
# They are unordered and dont allow duplicates
#syntax {}
set_of_numbers = {2,7,8}
set_of_numbers = {3,6,9}


#DICTIONARIES ,,,IS A collection that stores multiple values it allows u to
# Acesses values,, Change iems,, Add items,, Remove Item

student = {
   'name' : "Gillian",
   'age' : 20,
   'location' : 'Muyenga'
}
print(student)

Fruits={
   1: 'Apple',
   2: 'Orange',
   3: 'Banana'
}
print(Fruits)

#  Accessing the value
print(student['name'])
print(student['age'])
print(student['location'])


#Print the keys of the student dictionary
print(student.keys())

#Accesing the length function
print(len(student))

#add a key contact to the dictionary
student['contact'] = '0772676815'
print(student)

#Changing item,,,update the name Gillian to Apio
student['name'] = 'Apio Gilian'
print(student)

#Print all the values of a dictionary
print(student.values())
print(student)

#Remove the contact key from the dictionary ,,delete,remove,pop
student.pop('contact')
print(student)

#OOP....Object Oriented Programing ,,,,,,,,it has classes and objects
#Cohort class

























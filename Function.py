#DEFINITION
#Are used to perform specific task
#def, define a function
#Name, give it a function name():
#Function body
#Parameters(data information or variable)
#Arguments(value)
#Call a function depending on how u created[using the same naming conventions] it and out of the body

#Create a function that returns the main components of a function
def function_basic():
   print(f'The main components of functions are Parameters and Arguments\n')

function_basic()

#Create a function that returns your students name, registration number and your students age
def student_details():
  student_name = 'Mary' #local variables
  student_number = 'DCS/007/2024'
  student_age = '21'
  print(f'My name is {student_name} and i am {student_age} years old, my registration nunber is {student_number}')
student_details()

#Create a function that returns your students name, registration number and age as parameters
def students_data(students_name,students_age,students_reg):
   print(f'My name is {students_name} am {students_age} years young having reg number {students_reg}.')

students_data('Blessings','20','2024/007/SS')
   

   #RETURN VALUES
def my_name():   #we can use return instead of print but it does not give output, u have to contiue and print
   name = 'Mariah'
   return name
my_name()
#To view the output,
name = my_name()
print(name) 

#OR
def my_other_name():
   other = 'Rose'
   return other
my_other_name()

#OR
def her_name(names):
   return'I like my own, {names}'
her_name('Mistica')

#Create a function that calculates the area of a triangle.The base and the height must be aparameter.
def area(base,height):
   area = (1/2)*base*height
   print(f'The area of the triangle is {area}')

area(2, 4)

def triangle_area():
   base = int(input('Enter the base here:'))
   height = int(input('Enter the height here:'))
   areas = int((1/2)*base*height)
   print( f'The areas of the triangle is {areas} ')


   # DATA COLLECTION

#list , it has an acronym[ CRUD ],Create / Read / Update / Delete
# Here we use varname=[]
#list are array like structures, by use of indexing

my_friends = ['Joy', 'Palma', 'Raphela', 'Kabeisa' ] #strings
their_marks = [ 60, 82, 77, 68, ] #intergers

print(my_friends, type(my_friends))

#accesing items in the list,, 
# here  we use the index[0,1,2,3,4,5,6......] positve index  0r[-1,-2,-3,-4]negative index
print(my_friends[0])
print(my_friends[1])
print(my_friends[2])
print(my_friends[3])
print(my_friends[-1])
print(my_friends[-2])
print(my_friends[-3])


#Adding new items to the list
my_friends.append('Mercy')
print(my_friends)


#At aparticular position
my_friends.insert(2,'Patrick')
print(my_friends)

#test two > functions,For loops,List dictionaries
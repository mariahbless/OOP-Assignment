#write a program that takes two numbers as input and displays their sum, their difference, products and quotient.
number_one= int(input("Enter the first number: "))
number_two= int(input("Enter the second number: "))
sum=number_one + number_two
print(f"The sum of {number_one} and {number_two}")
print("The sum is " + str(sum))

difference=number_one - number_two
print(f"The difference of {number_one} and {number_two}")
print("The difference is " + str(difference))

product=number_one*number_two
print("The product is " + str(product))
print(f"the product of {number_one} and {number_two} is {product} ")

#write a program that compares two intergers and prints 
# weather the first number is greater than,less than or equals to the second number.
# if loops connects comparison if its true or false
if number_one > number_two :
    print(f" {number_one} is greater than {number_two}")
elif number_one < number_two :
    print(f" {number_one} is less than {number_two}")
else :
    print('They are not equal')

#1 write a program that checks if a given number is between 10 and 20 using logical operator
#  whereby [20 is inclusive using logical operator]
number = int(input("enter the number: "))
if 10 <number <= 20:
    print(f" {number} is between 10 and 20 (20 inclusive)")
else:
    print(f" {number} is not between 10 and 20 (20 inclusive)")   

#2 write a program that prints the squares of all intergers from 1 to 10 using afor loops
integers = [1,2,3,4,5,6,7,8,9,10]
for x in integers: 
      x= x**2
      print(x)

#3 Write a simple program that ask a user for their age if the user is greater or equals to 18,
#print you are an adult and you qualified
#else you are not qualified.
age = input("Enter your age:")
qualified_adults = "18"
if age >= qualified_adults:
    print(f"You are an adult and you are qualified")
else:
    print(f"You are not qualified")


#4 we have the following student details and marks enter these details from the keyboard
#students name = Ritah liz
#students number=sep23/bcs/14
#programming = 78
#data science = 89
#computer application = 55
#caltulate the average mark and print the answer in 3dps
student_name =input("Enter your student name: ")
student_nunber =input("Enter your student number: ")
programming = int(input("Enter marks scored in programming: "))
data_science = int(input("Enter marks scored in data science: "))
computer_application = int(input("Enter marks scored in computer application: "))

tota_mark = programming + data_science + computer_application
number_of_course_units = 3
average_mark = tota_mark / number_of_course_units
print(f"The average mark is : {average_mark:.3f} ")
average_mark = round(tota_mark/number_of_course_units,3)


#5 write the program that converts celcious temp to farenheit temp, 
# the program should ask the user to enter th temp in celcious degree and display the temperature converted to farenheit degrees.
temperature_in_celicius = float(input("Enter the temperature in celicious degree"))
degree_in_farenheit = (1.8* temperature_in_celicius) + 32
result = temperature_in_celicius / degree_in_farenheit
print(f"The result is: {result}")
#Formula for converting farenheit to celicious degree=9/5C + 32
#celcious to fareinheit F-32 /1.8, F = 9/5c +32, C =F-32/1.8


#6 Acar"s miles per gallons can be calculated with the following formulas.
#  write aprogram that calculates the number of miles driven and  gallons used
#  it should calculate the cars miles-per gallons used and display the results.,
#  And this is the formulae MPG = Miles driven/gallons of car used.
miles_driven = int(input("Enter the number of miles driven"))
gullons_used = int(input("Enter the number of gullons used"))
mpg = miles_driven / gullons_used
print(f"The cars miles driven per gullons was: {mpg}")

#OOP rep object Oriented Programming
#here we create a class first and it starts with a cpital letter 

#Assignment
#Add a constructor for the cohort class and add 
#to the method the class that prints the cohort class name
#and the Total number of students Create a new instance/object of the cohort class

class Cohort: #define the class
        def  _init_(self,name,student_total_num):
            

           self.name =  name
           self.student_total_num = student_total_num
        def print_cohort_info(self):#This is amethod that prints the cohort name and the cohort class
          print(f"Cohort's name: {self.name}")
          print(f"The total number of students in the cohort is: {self.student_total_num}")

          
cohort4 = Cohort("Python class cohort iv", 50) #this is the object of the cohort class
cohort4.print_cohort_info()#calling the method to print the details of the cohort
#OPERATOR PRECEDENCE, Control flow structures,conditional statement, loops
#defn this describes the order in which operation are performed in an expression,
#  operators with higher precidence are always executed first

results = 3*4+5
print(results)

result1 = 3*4+5-1
print(result1)

result2 = 3*(4+5)-1
print(result2)

result3 = 3*(4+5)/1
print(result3)

result4 = 5*3**2
print(result4)
result5 = (5+3)*2**2-10/2
print(result5)
result6 = 25/5+2*1
print(result6)


#CONTROL FLOW STRUCTURE
#This controls and determines the order in which the program is executed basing on loops and conditions.it uses conditional statement

#Creates aprogram that ask a user for the food type bought from the market
#  the progaram should print you bought chicken if the user enters chicken
# liver if the user enters liver

food_type = input('Enter the food type bought:,') .lower()

print(f"Please choose from chicken,liver,fish") 
if food_type == 'chicken':
    print(f"You bought chicken from the market")
elif food_type == 'liver' :
    print(f"You bought liver from the market")
elif food_type == 'fish' :
    print(f"You bought fish from the market")
else:
    print(f'You didnt buy any of the foods either liver,fish and chicken')

#OR

food_type = input('Enter the food type bought:,') .lower()
if food_type != 'chicken' or food_type != 'liver' or food_type != 'fish':
 print(f"Please choose from chicken,liver,fish") 
if food_type == 'chicken':
    print(f"You bought chicken from the market")
elif food_type == 'liver' :
    print(f"You bought liver from the market")
elif food_type == 'fish' :
    print(f"You bought fish from the market")
else:
    print(f'You didnt buy any of the foods either liver,fish and chicken')


#OPERATORS
#Arithmetic operator
#eg addition +,subtraction -,division /,-, multiplication *, modulas // [takes the remainder],floor division

#COMPARISON OPERATORS[USE OF IF LOOPS]
# greater than[>] (9>2)=true
# less than[<] (9<2)=false
# equals to[=] (9=2)=false
# not equal to[!=] (9!=2)=true
 

#ASSIGNMENT OPERATORS
sum = 6
sum + 5
print(sum + 5)

#given that we have two products a laptop and a mouse such that the price of a mouse is 50000 and a laptop is 300000
#  use a for loop to find the total sum of the products
laptop = 300000
mouse = 50000
sum = 0

product_prices = [laptop, mouse]
for price in  product_prices:
    sum += price
print(f"The total sum of the product is: {sum:,} ")

 #practice questions
 

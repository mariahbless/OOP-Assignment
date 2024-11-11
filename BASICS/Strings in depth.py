 #STRINGS IN PYTHON
#Array like structure {The first index is always o,1,2,3.....}
#Array list eg
#marks = [90,60,70,80]
name="mariah"
print(name[0])
#print the last word in the name mariah
print(name[5])

#LOOPING THROUGH STRINGS
#We loop through strings using a keyword "for"
#eg
for character in name:
    print(character)
address="kamokya"
for item in address:
    print(item)

#SLICING IN STRINGS
#Accessing a range of characters in a string
#eg
name="agnes"
print(name[1:4])
name="pineapples"
print(name[4:9])
name="jesus"
print(name[0:5])

#NEGATIVE INDEXING[it starts from the left]
#Eg
message="hello"
print(message[-1])
print(message[-1:-4])
print(message[-1:-5])
print(message[-5:-3])
print(message[-4:])
print(message[4:])


# F- STRINGS [Formatted strings]
name="Rose"
age="50"
wieght=68.4
print(" My mum's name is " + name + " her age is " + age)
print(f"my mum is {name} and she is {age} years old and she weighs {wieght:1f} ")
total_cost=300000
print(f"my rent has been inreased to {total_cost:,}")


# STRING LENGTH[ITS ALL ABOUT THE NUMBER OF CHARACTERS]
name="royal\n Mary\n"
print(name)
print(name.upper)
address=" from kamwokya"
print(len[address])

name ="pineapple"
print(name[4:9])
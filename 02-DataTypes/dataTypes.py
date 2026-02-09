import math

# Literal Assignment

first = 'Raka'
last = 'Maharjan'

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# # Constructor Function

# pizza = str('Pepperoni')
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

#Concatenation

# fullname = first + ' ' + last
# print(fullname)

# fullname += "!"
# print(fullname)

# Casting a number to a string

# decade = str(1980)
# print(type(decade))
# print(decade)

# statement = 'I like rock music from the' + decade + 's.'
# print(statement)

# Multiple Lines

# multilines = '''
# Hey, how are you ?

# I was just checking in.
#                                     All good ?
# '''
# print(multiplelines)

# #Escaping special characters

# sentence = 'I\'m back at the work!\tHey!\n\nWhere\'s this at located?'
# print(sentence)

#String Methods
# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

# print(multilines.title())
# print(multilines.replace('checking','coming'))
# print(multilines)

# print(len(multilines))
# multilines += '                                                     '
# multilines += '         ' + multilines
# print(len(multilines))

# print(len(multilines.strip()))
# print(len(multilines.lstrip()))
# print(len(multilines.rstrip()))

#Build a menu
# title = 'menu'.upper()
# print(title.center(20,'='))
# print("Coffee".ljust(15,'.') + "$2.68".rjust(4))
# print("Latte".ljust(15,'.') + "$3.68".rjust(4))
# print("Americano".ljust(15,'.') + "$4.68".rjust(4))

# print('')

# String Index Value

# print(first[0])
# print(first[1])
# print(first[2])
# print(first[3])
# print(first[-3])
# print(first[-2])
# print(first[-1])
# print(first[0])

# print(first[1:])
# print(first[1:3])
# print(first[1:-1])

# Some methods return boolean data
# print(first.startswith('A'))
# print(first.endswith('a'))


#Boolean Data type
# myValue = True
# x = bool(False)
# print(type(x))
# print(isinstance(myValue, bool))

#Numeric Data Types
# price = 100
# best_price = int(80)
# print(type(price))
# print(isinstance(best_price, int))

#Float Type
# gpa = 3.5
# y = float(1.45)
# print(type(gpa))
# print(isinstance(y, float))

#complex type

# value = 4 + 2j
# print(type(value))
# print(value.real)
# print(value.imag)

# Built-in functions for numbers

gpa = 3.54
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa,1))

print('')

print(math.pi)
print(math.sqrt(64))
print(int(math.sqrt(64))) # Convert float to an integer
print(math.ceil(gpa))
print(math.floor(gpa))

#Casting string to a number
zipcode = "100010010"
zipvalue = int(zipcode)
print(zipvalue)
print(type(zipvalue))


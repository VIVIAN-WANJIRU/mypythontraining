#integers are numbers without a decimal
#float are numbers with decimals
#booleans True or False 

#Arithmetic operators +,-,*,/,%
#Conditional operators <,>,<=,==
#Logical operaators 
#  and - all conditions (i < 7 and i > 5)
#  or - atleast one condition to be true
#  in - contains

num1=80

num2=30

total = num1 + num2 

print((6>7) or (7==7))

print('@' in 'mail@mail.com')

print('@' in 'mail@mail.com' and '.' in 'mail@mail.com')
temp = 56.8926
temp = round(temp,3)
print(temp)


temp = 56.8926
temp = round(temp,2)
temp = str(temp) + "0"
print(temp)

temp = 56.8926
temp = str(temp)[0:6]
print(temp)

temp_three = 56.8926
temp_three = str(temp_three)
temp_three = temp_three[3] + temp_three[2] + temp_three[4:7]
print(temp_three)



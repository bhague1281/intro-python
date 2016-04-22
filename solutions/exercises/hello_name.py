# print my name
print('Hello Brian!')

age = 32
print(age)

days = age * 365.26
print('I am ' + str(days) + ' days old')

# divisible_by_4 = age % 4 == 0
if age % 4 == 0:
    print('My age is divisible by 4')
else:
    print('My age is not divisible by 4')

if not age % 2:
    print('My age is even')
    if days > 1:
        print('Congrats, you\'re kinda old')
else:
    print('My age is odd')

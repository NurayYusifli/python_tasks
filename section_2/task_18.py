age = int(input('What is your age? '))
if age >= 18:
    print('Cinema ticket prices: 15$')
elif age >=13 and age <= 17:
    print('Cinema ticket prices: 10$')
else:
    print('Cinema ticket prices: 7$')
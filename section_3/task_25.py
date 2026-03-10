height = float(input('How much is  your height? '))
age = float(input('What is  your age? '))
if height < 120 and age < 18:
    print('You need parents')
else:
    print('Access granted')
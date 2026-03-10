degree = input('How much is  your degree? ')
experience = float(input('How much is  your experience? '))
age = float(input('What is  your age? '))
if (experience >= 5 or degree == 'CS') and (age >= 22 and age <= 45):
    print('You are hired')
else:
    print('You aren`t hired')
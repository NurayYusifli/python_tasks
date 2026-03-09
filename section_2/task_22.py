BMI = float(input('What is your BMI? '))
if BMI >= 30:
    print('Obese')
elif BMI >= 25 and BMI < 30:
    print('Overweight')
elif BMI >= 18.5 and BMI < 25:
    print('Normal')
else:
    print('Underweight')
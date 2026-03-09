# Ask for  and height (m). Calculate . Print the result.
weight  = float(input('What is weight (kg): '))
height  = float(input('What is height (m): '))
BMI = weight / pow(height,2)
print(f'Result: {BMI}')
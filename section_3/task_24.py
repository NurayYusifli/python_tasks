temp = float(input('How much is room of temp? '))
if temp >= 30:
    print('Do you want AC')
elif temp >= 20 and temp < 30:
    print('Comfortable')
else:
    print('Do you want heater')
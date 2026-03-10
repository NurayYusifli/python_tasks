member = input('Are you member? /y/n')
order = float(input('How many are your orders? '))
if order >= 100:
    print('Postage: 0$')
else:
    if member == 'y':
        print('Postage: 3$')
    else:
        print('Postage: 7$')

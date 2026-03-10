income = float(input('How much is your income? '))
credit = float(input('How much is your credit? '))
if income > 50000 and credit > 700:
    print('Loan approved')
else:
    print('Loan denied')
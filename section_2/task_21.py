# Ask for a year. A leap year is divisible by 4, except centuries unless divisible by 400.
year = int(input('Enter a year: '))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f'{year} is leap year')
else:
    print(f'{year} isn`t leap year')
# Ask for a month number (1-12). Print the season: (3-5), (6-8), (9-11), Winter(12,1,2).
month = int(input('What month is it now? '))
if month >= 1 and month <= 12:
    
    if month == 1 or month == 2 or month == 12:
        print('Winter') 
    elif month == 3 or month == 4 or month == 5:
        print('Spring')
    elif month == 6 or month == 7 or month == 8:
        print('Summer')
    else:
        print('Autumn')
else:
    print('Write between 1 and 12 numbers')
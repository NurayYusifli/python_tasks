score = float(input('Take a score: '))
if score <=100:
    if score >= 60:
        print('Pass')
    else:
        print('Fail')
else:
    print('score between 1 and 100')
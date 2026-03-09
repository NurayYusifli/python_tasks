# Ask for a score. Print grade: A(90+), B(80+), C(70+), D(60+), F(below 60).
score = float(input('What is your score? '))
if score <=100:
    if score > 90:
        print('A')
    elif score > 80:
        print('B')
    elif score > 70:
        print('C')
    elif score > 60:
        print('D')
    elif score > 50:
        print('F')
    else:
        print('E')
else:
    print('score between 1 and 100')
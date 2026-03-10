import random
num = random.randint(1, 100)
# print(num)
s = 1
while True:
    n = int(input('Enter a number: '))
    s += 1
    if n < 100:
        if n == num:
            print('equal')
            break
        elif n < num:
            print('Higher')
        elif n > num:
            print('Lower')
        else:
            print('not equal')
    else:
        print('between 1 and 100')

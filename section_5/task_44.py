n = int(input('Enter a pair of number: '))
while n != 1:
    s = n % 2
    match s:
        case 0:
            n = n // 2
        case 1: 
            n = 3 * n + 1
    print(n)
print('Finish!')
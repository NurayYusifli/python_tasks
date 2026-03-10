n = int(input('Enter a odd number: '))
if n % 2 == 0:
    print('Enter a odd number!')
else:
    for i in range (1, n + 1, 2):
        s = (n - i) // 2
        print(" " * s + "*" * i)
    for i in range (n - 2, 0, -2):
        s = (n - i) // 2
        print(" " * s + "*" * i)
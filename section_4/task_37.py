n = int(input('Enter a number: '))
s = True
for i in range (2, n + 1):
    if n % i == 0:
        s = 'Not Prime'
    else:
        s = 'Prime'
print(s)
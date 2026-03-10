n = int(input("How many Fibonacci numbers? "))
a = 0
b = 1
s = 0
if n <= 0:
    print('Enter a pair of number: ')
elif n == 1:
    print(a)
else:
    while s < n:
        print(a, end=" ")
        a, b = b, a + b
        s += 1
num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))
while num_2 != 0:
    num_1, num_2 = num_2, num_1 % num_2
print(num_1)

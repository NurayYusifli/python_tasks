# Ask for 3 numbers. Find and print the largest using if/elif/else (no built-in max()).
num_1 = float(input('Take the first number: '))
num_2 = float(input('Take the second number: '))
num_3 = float(input('Take the third number: '))
if num_1 > num_2:
    if num_1 > num_3:
        max = num_1
    else:
        max = num_3
else:
    if num_2 > num_3:
        max = num_2
    else:
        max = num_3
print(f'The largest number: {max}')
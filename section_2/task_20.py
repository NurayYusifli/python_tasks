length_1 = float(input('What is first length? '))
length_2 = float(input('What is second length? '))
length_3 = float(input('What is third length? '))
if length_1 + length_2 > length_3 and length_1 + length_3 > length_2 and length_2 + length_3 > length_1:
    print(' A valid triangle')
else:
    print(' Not a valid triangle')
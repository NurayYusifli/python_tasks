s = 0
while True:
    num = float(input("Enter a number (0 to stop): "))
    if num == 0:
        break    
    s += num
    print(s)
print(f"total: {s}")
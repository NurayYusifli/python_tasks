password = input('Enter a password: ')
l = len(password)
r = False
for i in password:
    if i.isdigit():
        r = True
        break
h = False
for i in password:
    if i.isupper():
        h = True
        break
while True:
    if l >= 8 :
        if r == True:
            if h == True:
                print('Access Granted')
                break
            else:
                print('Enter a uppercase letter')
                break
        else:
            print('Enter a digit')
            break
    else:
        print('Enter 8+ chars')
        break
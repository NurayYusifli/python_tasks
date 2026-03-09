print("Sign up")
username_first = input('Enter the username: ')
password_first = input('Enter the password: ')

print("Log in")
username = input('Enter the username: ')
password = input('Enter the password: ')

if username_first == username and password_first == password:
    print('Access Granted')
else:
    print('Access Denied')
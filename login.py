print('Create account now')
username = input('Enter username: ')
password = input('Enter password: ')

print('Your account has been created successfully')
print('Login now!')

username2 = input('Enter usename: ')
password2 = input('Enter Password: ')

if username == username2 and password == password2:
    print('Logged in successfully')
else:
    print('Invalid credentials')
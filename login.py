import string
user = input('Username: ')
if not user:
    print('Please inform your username!')
elif user:
    password = input('Password: ')
    if not password:
        print('Please inform your password!')

str1 = ''

if user and password:
    if len(password) >= 8 and user:
        for i in password:
            if i.isalpha():
                str1 += 'A'
            elif i.isdigit():
                str1 += 'D'
            elif i in string.punctuation:
                str1 += 'P'
    elif len(password) < 8:
        print('Password must have at least 8 characters!')

if user and password:
    if 'A' in str1 and 'D' in str1:
        print('Login already!')
    elif 'A' in str1 and 'D' in str1 and 'P' in str1:
        print('Login already!')
    else:
        print('Please inform number and alpha too!')
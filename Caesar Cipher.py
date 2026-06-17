print('---Welcome to secret password generator---')
choice = input('Encrypt(E) or Decrypt(D)? ')
msg = input('Enter your message: ')
key = int(input('Enter the length of your secret password: '))
new_msg = ''

if choice.upper() ==  'E':
    length = len(msg)
    for i in range(length):
        new_msg += chr(ord(msg[i]) + key)
    print(new_msg.upper())
elif choice.upper() == 'D':
    length = len(msg)
    for i in range(length):
        new_msg += chr(ord(msg[i]) - key)
    print(new_msg.upper())



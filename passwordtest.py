with open('passwords.txt', 'r') as file:
    password = file.read().rstrip('\n')

print(password)
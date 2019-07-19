import sys
while True:
    print('if you want to finish, input exit')
    response = input()
    if response == 'exit':
        sys.exit()
    print(response + 'is input')

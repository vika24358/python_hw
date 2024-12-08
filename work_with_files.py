# my_file = open('main.py')
# print(my_file)
#
# print(my_file.read())
# print(my_file.closed)
# my_file.close()

# with open('main.py') as my_file, open('functions.py') as functions_file:
#     print(my_file.read())
#     print(functions_file.read())


def create_log(log: str, filename: str = 'new_file.txt'):
    with open(filename, mode='a+') as my_file:
        my_file.write(f'\n{log}')


create_log(log='kdkfkfkfkf')


def read_log(filename: str = 'new_file.txt'):
    with open(filename, mode='r') as my_file:
        logs = my_file.read()
        print(logs.split())
        my_file.seek(0)
        data = my_file.readlines()
        print(data)

# read_log()
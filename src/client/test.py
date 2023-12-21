import os

up_three_folders = os.path.abspath(os.path.join(os.getcwd(), '../../..'))

file_name = 'data/test.txt'

with open(file_name, 'r') as file:
    content = file.read()
    print(content)

import os

path = "test.txt"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location doesn't exist!")

try:
    # zamyka automatycznie
    with open(path) as file:
        print(file.read())

    print(file.closed)
except FileNotFoundError:
    print("That file was not found")


import os

source = "text.txt"
destination = "C:\\Users\\micha\\Desktop\\text.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)  # może być folderem!
        print("File moved")
except FileNotFoundError:
    print(source+" was not found")

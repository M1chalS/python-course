import time

# while 1 == 1:
#     print("Help Im stuck in a loop")

name = ""

while not name:
    name = input("Enter your name: ")

print("Hello "+name)

for i in range(10):
    print(i)

for i in range(50,100+1,2):
    print(i)

for i in "Robert":
    print(i)


for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy new year!")

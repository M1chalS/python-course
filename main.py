# string
name = "Michał"
print("Your name is: " + name)
print(type(name))

# int
age = 25
# str = toString()
print("Your age is: " + str(age))
print(type(age))

# float
height = 250.5
print("Your height is: " + str(height) + "cm")
print(type(height))

# boolean
human = True
print("Are you a human: " + str(human))
print(type(human))

# multiple assignment
name, age, attractive = "Michał", 19, True

print(name, age, attractive)

Spongebob = Patrick = Sandy = Squidward = 30

print(Spongebob, Patrick, Sandy, Squidward)

# string methods
name = "michał"


print(len(name))  # length
print(name.find("i"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())  # is number
print(name.isalpha())  # is alphabetical letters
print(name.count("a"))
print(name.replace("a","o"))
print(name*4)

# type casting int(), str(), float()
x = 1
y = 2.0
z = "3"

y = int(y)
z = float(z)
x = str(x)

print(x)
print(y)
print(z*3)

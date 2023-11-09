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
print(name.replace("a", "o"))
print(name * 4)

# type casting int(), str(), float()
x = 1
y = 2.0
z = "3"

y = int(y)
z = float(z)
x = str(x)

print(x)
print(y)
print(z * 3)

# string slicing [start:stop:step]
name = "Robert Kubica"

first_name = name[0:6]  # [:6] od 0 do 6
last_name = name[7:13]  # [7:] od 7 do końca
funky_name = name[::2]  # [::2] od początku do końca z przejściem o dwa
reversed_name = name[::-1]

print(first_name, last_name, funky_name, reversed_name)

website1 = "https://google.com"
website2 = "https://wikipedia.com"

Slice = slice(8, -4)

print(website1[Slice])
print(website2[Slice])

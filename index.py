name = "robert Kubica!"

if name[0].islower():
    name = name.capitalize()

print(name)

first_name = name[:6].upper()
last_name = name[7:].lower()
last_character = name[-1]

print(first_name, last_name, last_character)

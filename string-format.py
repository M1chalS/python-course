animal = "cow"
item = "moon"

print("The {} jumper over the {}".format(animal, item))
print("The {1} jumper over the {0}".format(animal, item))  # positional argument
print("The {animal} jumper over the {item}".format(animal="cow", item="moon"))  # positional argument

text = "The {} jumped over the {}"
print(text.format("cow", "moon"))

name = "Robert"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))
print("Hello, my name is {:<10}. Nice to meet you".format(name))  # align left
print("Hello, my name is {:>10}. Nice to meet you".format(name))  # align right
print("Hello, my name is {:^10}. Nice to meet you".format(name))  # align center
print("Hello, my name is {name:^10}. Nice to meet you".format(name=name))  # align center

number = 3.14159
number2 = 4444

print("The number pi is {:.2f}".format(number))  # dwie po przecinku
print("The number pi is {:,}".format(number2))  # auto przecinek
print("The number pi is {:b}".format(number2))  # binary 2
print("The number pi is {:o}".format(number2))  # octo 8
print("The number pi is {:x}".format(number2))  # hex 16
print("The number pi is {:e}".format(number2))  # scientific


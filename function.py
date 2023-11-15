# def hello(first_name, last_name, age):
#     print("Hello " + first_name + " " + last_name)
#     print("You are " + str(age) + " years old")
#     print("Have a nice day!")
#
#
# hello("Robert", "Kubica", 40)
#
#
# def multiply(number1, number2):
#     return number1 * number2
#
#
# result = multiply(4, 8)
#
# print(result)
#
#
# def say_hello(first, middle, last):
#     print("Hello " + first + " " + middle + " " + last)
#
#
# say_hello(last="Kubica", middle="Driver", first="Robert")
#
# # num = round(abs(float(input("Enter a whole positive number: "))))
# #
# # print(num)
#
# first_name = "Robert"
# last_name = "Kubica"
#
#
# # Local -> Enclosing -> Global -> Built-in
# def display_name():
#     first_name = "Driver"
#     print(first_name, last_name)
#
#
# print(first_name, last_name)
# display_name()
#
#
# def add(*args):
#     sum = 0
#     args = list(args)
#     args[2] = 4
#     for i in args:
#         sum += i
#     return sum
#
#
# print(add(1, 2, 3, 4, 5, 6))


def say_hello_again(**kwargs):
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


say_hello_again(title="Jednoręki", first_name="Robert", middle="Driver", last_name="Kubica")

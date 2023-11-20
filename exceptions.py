try:
    numerator = int(input("Enter a numer to divide: "))
    denominator = int(input("Enter a numer to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print("You can't divide by zero!", e)
except ValueError as e:
    print("Enter only numbers!", e)
except Exception as e:
    print("something went wrong :(", e)
else:
    print(result)
finally:
    print("This will always execute")

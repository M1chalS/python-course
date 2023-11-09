temp = int(input("What is the temperature outside?: "))

if not(temp >= 0 and temp <= 30):
    print("the temperature is bad today!")
elif not(temp < 0 or temp > 30):
    print("the temperature is good today!")
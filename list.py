food = ["pizza", "hamburger", "hotdog", "spaghetti"]

food[0] = "sushi"

# print(food)

food.append("ice cream")
food.remove("hotdog")
food.pop()  # usunięcie ostatniego elementu
food.insert(0, "cake")  # nie zastępuje tylko przesuwa
food.sort()
# food.clear()

print("List 1:")
for x in food:
    print(x)

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
desert = ["cake", "ice cream"]

food = [drinks, dinner, desert]

print("List 2:")
print(food[0])

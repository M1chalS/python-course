capitals = {
    "USA": "Washington DC",
    "India": "New Dehli",
    "China": "Beijing",
    "Poland": "Warsaw"
}

print(capitals.get("USA"))
print(capitals.get("Germany"))  # Jak nie ma zwraca None

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Las Vegas"})
capitals.pop("China")
# capitals.clear()

print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
    print(key, value)

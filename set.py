utensils = {"fork", "spoon", "knife"}  # wartości zawsze są unikalne i niepoukładane
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin")
utensils.remove("fork")
# utensils.clear()
# utensils.update(dishes)  # nie zwraca
dinner_table = utensils.union(dishes)  # zwraca

# print(dishes.difference(utensils))  # to czego nie ma w drugim
print(utensils.intersection(dishes))  # to, co jest częścią wspólną obu

for x in dinner_table:
    print(x)

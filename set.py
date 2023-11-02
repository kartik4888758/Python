fruits_set = {"apple", "banana", "cherry", "date"}
citrus_set = {"orange", "lemon", "lime", "date"}

fruits_set.add("grape")
print(f"Fruits set after adding 'grape': {fruits_set}")

citrus_set.remove("lime")
print(f"Citrus set after removing 'lime': {citrus_set}")

combined_set = fruits_set.union(citrus_set)
print(f"Combined set of fruits and citrus: {combined_set}")

common_fruits = fruits_set.intersection(citrus_set)
print(f"Common fruits in both sets: {common_fruits}")

is_subset = common_fruits.issubset(fruits_set)
print(f"Are common fruits a subset of fruits set? {is_subset}")

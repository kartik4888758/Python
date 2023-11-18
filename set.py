fruits_set = {"apple", "banana", "cherry", "date"}
citrus_set = {"orange", "lemon", "lime", "date"}

fruits_set.add("grape")
print(f"after adding: {fruits_set}")

citrus_set.remove("lime")
print(f"Citrus set: {citrus_set}")

combined_set = fruits_set.union(citrus_set)
print(f"Combined set : {combined_set}")

common_fruits = fruits_set.intersection(citrus_set)
print(f"Common fruits: {common_fruits}")

is_subset = common_fruits.issubset(fruits_set)
print(f"Are common fruits a subset of fruits set? {is_subset}")

original_list = [1, 2, 3, 4, 5]

aliased_list = original_list
aliased_list.append(6)

cloned_list = original_list.copy()
cloned_list.append(7)

print("Original List:", original_list)
print("Aliased List:", aliased_list)
print("Cloned List:", cloned_list)

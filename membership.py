fruits = ["apple", "banana", "cherry"]

fruit_to_check = "banana"
if fruit_to_check in fruits:
    print(f"Yes, {fruit_to_check} is in the list.")
else:
    print(f"No, {fruit_to_check} is not in the list.")

fruit_to_check = "grape"
if fruit_to_check not in fruits:
    print(f"Yes, {fruit_to_check} is not in the list.")
else:
    print(f"No, {fruit_to_check} is in the list.")

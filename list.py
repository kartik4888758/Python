fruits = ["apple", "banana", "cherry"]

fruits.append("date")
print(f"Fruits after appending: {fruits}")

fruits.insert(1, "grape")
print(f"Fruits after inserting: {fruits}")

fruits.remove("cherry")
print(f"Fruits after removing 'cherry': {fruits}")

popped_fruit = fruits.pop()
print(f"Popped fruit: {popped_fruit}, Fruits after popping: {fruits}")

index = fruits.index("banana")
print(f"Index of 'banana': {index}")

count = fruits.count("apple")
print(f"Count of 'apple': {count}")

fruits.reverse()
print(f"Reversed fruits: {fruits}")

fruits.sort()
print(f"Sorted fruits: {fruits}")

copied_fruits = fruits.copy()
print(f"Copied fruits: {copied_fruits}")

fruits.clear()
print(f"Fruits after clearing: {fruits}")

text = "Hello, World!"

length = len(text)
print(f"Length of the string: {length}")

uppercase_text = text.upper()
print(f"Uppercase: {uppercase_text}")

count = text.count("l")
print(f"Count of 'l': {count}")

position = text.find("World")
print(f"Position of 'World': {position}")

new_text = text.replace("World", "Python")
print(f"Replaced text: {new_text}")

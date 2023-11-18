import string

print(f"Uppercase letters: {string.ascii_uppercase}")
print(f"Lowercase letters: {string.ascii_lowercase}")
print(f"Digits: {string.digits}")
print(f"Punctuation: {string.punctuation}")
print(f"Whitespace characters: {string.whitespace}")

numeric_str = "12345"
non_numeric_str = "Hello"
print(f"'{numeric_str}' is numeric: {numeric_str.isnumeric()}")
print(f"'{non_numeric_str}' is numeric: {non_numeric_str.isnumeric()}")

name = "John"
age = 30
formatted_text = f"My name is {name} and I am {age} years old."
print(formatted_text)

repeated_text = "Python " * 3
print(f"Repeated text: {repeated_text}")

text = "Python is HLL"
substring = text[7:9]
print(f"Sliced substring: {substring}")

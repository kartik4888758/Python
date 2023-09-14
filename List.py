languages=["C","C++","Java"]
print(languages)

languages.append("Python")
print(languages)

languages.clear()
print(languages)

languages=["C","C++","Java"]
x=languages.copy()
print(x)

languages=["C","C++","Java","Java"]
x=languages.count("Java")
print(x)

languages=["C","C++","Python","HTML","Java"]
languages.sort()
print(languages)
languages.reverse()
print(languages)

fruit=["apple","mango"]
languages.extend(fruit)
print(languages)

languages.pop()
languages.pop(2)
print(languages)
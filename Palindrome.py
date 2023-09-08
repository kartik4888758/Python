word = input("Enter a string: ")


word = word.replace(" ", "").lower()

if word == word[::-1]:
    print("Palindrome found.")
else:
    print(" Not a palindrome.")

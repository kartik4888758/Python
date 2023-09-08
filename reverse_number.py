num = int(input("Enter a number: "))
new = 0
while num > 0:
    last_digit = num % 10
    new = new * 10 + last_digit
    num = num // 10
print("Reversed number:", new)

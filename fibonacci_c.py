terms=int(input("enter number of term for series:"))
a, b = 0, 1


if terms <= 0:
        print("Please enter a positive integer.")
else:
        print("Fibonacci Series:")
for _ in range(terms):
    print(a, end=" ")
    a, b = b, a + b

first=int(input("enter first number:"))
second=int(input("enter second number:"))
third=int(input("enter third number:"))

if first>second and first>third:
    print(first,"is largest number.")
elif second>first and second>third:
    print(second,"is largest number.")
else:
    print(third,"is largest number.")
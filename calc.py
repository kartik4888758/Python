first=input("enter first number:")
second=input("enter secomd number:")
operator=input("enter operator (+,-,*,/,%):")

first=int(first)
second=int(second)
if operator =="+":
    print(first+second)
elif operator =="-":
    print(first*second)
elif operator =="/":
    print(first/second)
elif operator =="%":
    print(first%second)
else:
    print("invalid operation.")   
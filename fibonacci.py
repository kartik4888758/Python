# a = int(input("Enter the number of terms: "))
# A, B = 0, 1

# print("the Fibonacci Series:")
# for i in range(a):
#     print(A, end=" ")
#     A, B = B, A + B
# Input the number of terms
upto = int(input("Enter the number of Fibonacci terms: "))

# Initialize the first two terms
a, b = 0, 1


if upto <= 0:
    print("Please enter a positive integer.")
else:
    
    print("Fibonacci Series:")
    for _ in range(upto):
        print(a, end=" ")
        a, b = b, a + b

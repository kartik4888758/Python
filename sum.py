# a=int(input("enter natural number for sum:" ))
# b=(a*(a+1))/2
# print("The sum upto given natural number is:",b)

def sum(n):
    if n<=1:
        return n
    else:
        return n+sum(n-1)
num=int(input("enter number of term for sum:"))
if num<0:
    print("enter a positive number.")
else:
    print(sum(num))
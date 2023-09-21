# def fact(x):
#     if x==1:
#         return 1
#     else:
#         return (x*fact(x-1))
# num=5
# if num>=1:
#     print(fact(num))\
    
    
def fibo(n):
    if n<=1:
        return n
    else:
        return(fibo(n-1)+fibo(n-2))
n=int(input("enter term "))
if n<=0:
    print("number should be greater than zero.")
else:
    print("fibonacci sequence:")
    for i in range(n):
        print(fibo(i))
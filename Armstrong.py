n=int(input("enter number of digits:"))
num=int(input("enter a number:"))
sum=0

temp=num
while num>0:
    digit=num%10
    sum+=digit**n
    num=num//10
if temp==sum:
    print("It's Armstrong number.")
else:
    print("Not a Armstrong number.")
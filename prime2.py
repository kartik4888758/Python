num=int(input("enter a number:"))
for i in range(2,int(num)):
    if(num % i)==0:
        print("not prime")
        break
else:
    print("it's prime")
    
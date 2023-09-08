age=input("enter your age:")

if int(age)>=18:
    print("you are eligible to vote.")

elif int(age)<18 and int(age)>3:
    print("you are in school.")
else:
    print("you are child.")
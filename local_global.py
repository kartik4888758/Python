#here variable 'a' is global variable
a=5;

def add():
# here variable 'b' and 'c' are local variable
    b=10;
    c=a+b;
    print("The sum is",c,".")
add();

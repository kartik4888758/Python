def compound_interest(principal, rate, time, n):
    amount = principal * (1 + rate / (n * 100))**(n * time)
    interest = amount - principal
    return interest

# Input from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in percentage): "))
time = float(input("Enter the time period (in years): "))
n = int(input("Enter the number of times interest is compounded per year: "))

# Calculate and display the compound interest
compoundinterest = compound_interest(principal, rate, time, n)
print(f"Compound Interest: {compoundinterest}")

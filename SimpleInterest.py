def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

# Input from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in percentage): "))
time = float(input("Enter the time period (in years): "))

# Calculate and display the simple interest
simpleinterest = simple_interest(principal, rate, time)
print(f"Simple Interest: {simpleinterest}")

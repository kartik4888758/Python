import math

def calculate_emi(principal, rate, time):
    r = rate / (12 * 100)  
    n = time * 12  
    emi = (principal * r * math.pow(1 + r, n)) / (math.pow(1 + r, n) - 1)
    return emi


principal = float(input("Enter the loan amount: "))
rate = float(input("Enter the annual interest rate (in percentage): "))
time = float(input("Enter the loan tenure (in years): "))

emi = calculate_emi(principal, rate, time)
print(f"Monthly EMI: {emi:.2f}")

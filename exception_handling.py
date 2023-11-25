try:
    # ZeroDivisionError
    num1 = int(input("Enter a numerator: "))
    num2 = int(input("Enter a denominator: "))
    result = num1 / num2

    # ValueError
    value = int(input("Enter an integer value: "))

    # TypeError
    text = "Hello"
    concatenate = text + 5

    # FileNotFoundError
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()

except ZeroDivisionError:
    print("Error: Not divisible.")
except ValueError:
    print("Error: Please enter valid integers.")
except TypeError:
    print("Error: Type mismatch or unsupported operation.")
except FileNotFoundError:
    print("Error: The specified file was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

else:
    print(f"The result of {num1} / {num2} is: {result}")
    print(f"You entered the integer value: {value}")
    print(f"Concatenation result: {concatenate}")

finally:
    print("Finally block executed.")

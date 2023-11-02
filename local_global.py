global_var = "I am a global variable"

def example_function():
    global global_var
    local_var = "I am a local variable"
    print(f"Inside the function: global_var = {global_var}, local_var = {local_var}")

    global_var = "Global variable has been modified inside the function"

example_function()

print(f"Outside the function: global_var = {global_var}")

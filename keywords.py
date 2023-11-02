temperature = 30
if temperature > 25:
    print("It's a hot day.")
else:
    print("It's not very hot.")

colors = ["red", "green", "blue"]
for color in colors:
    print(f"The color is {color}.")

count = 0
while count < 3:
    print(f"Count is {count}.")
    count += 1

for num in range(10):
    if num == 5:
        break
    print(num)

for num in range(5):
    if num == 2:
        continue
    print(num)

for i in range(3):
    pass

numbers = [11, 22, 33, 44, 55]
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

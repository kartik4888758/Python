car_info = {
    "brand": "Toyota",
    "model": "Supra",
    "year": 2022,
    "color": "Silver",
    "price": 7500000
}

brand = car_info["brand"]
print(f"Car brand: {brand}")

car_info["year"] = 2023
print(f"Updated year: {car_info['year']}")

car_info["fuel_type"] = "Gasoline"
print(f"Added fuel type: {car_info['fuel_type']}")

del car_info["color"]
print(f"Dictionary after removing 'color': {car_info}")

key_exists = "price" in car_info
print(f"Is 'price' a key in the dictionary? {key_exists}")

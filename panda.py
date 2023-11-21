import pandas as pd

def pandas_example():
    # Create a DataFrame
    data = {'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 35],
            'City': ['New York', 'San Francisco', 'Los Angeles']}

    df = pd.DataFrame(data)

    # Display the DataFrame
    print("DataFrame:")
    print(df)

    # Accessing specific columns
    ages = df['Age']
    cities = df['City']

    # Displaying specific columns
    print("\nAges:")
    print(ages)

    print("\nCities:")
    print(cities)

if __name__ == "__main__":
    pandas_example()


#output

DataFrame:
    Name  Age           City
0  Alice   25       New York
1    Bob   30  San Francisco
2 Charlie   35    Los Angeles

Ages:
0    25
1    30
2    35
Name: Age, dtype: int64

Cities:
0         New York
1    San Francisco
2      Los Angeles
Name: City, dtype: object

import numpy as np

def numpy_example():
    # Create a 1D array
    arr1 = np.array([1, 2, 3, 4, 5])

    # Create a 2D array
    arr2 = np.array([[1, 2, 3], [4, 5, 6]])

    # Perform basic operations
    sum_arr = np.sum(arr1)
    mean_arr = np.mean(arr1)
    max_arr = np.max(arr2)

    # Perform element-wise operations
    square_arr = np.square(arr1)
    sqrt_arr = np.sqrt(arr1)

    # Create a random array
    rand_arr = np.random.rand(3, 3)

    # Print the results
    print("1D Array:", arr1)
    print("2D Array:", arr2)
    print("Sum of 1D Array:", sum_arr)
    print("Mean of 1D Array:", mean_arr)
    print("Max of 2D Array:", max_arr)
    print("Square of 1D Array:", square_arr)
    print("Square root of 1D Array:", sqrt_arr)
    print("Random 3x3 Array:", rand_arr)

if __name__ == "__main__":
    numpy_example()




#output

1D Array: [1 2 3 4 5]
2D Array:
 [[1 2 3]
  [4 5 6]]
Sum of 1D Array: 15
Mean of 1D Array: 3.0
Max of 2D Array: 6
Square of 1D Array: [ 1  4  9 16 25]
Square root of 1D Array: [1.         1.41421356 1.73205081 2.         2.23606798]
Random 3x3 Array:
 [[0.43248312 0.07682374 0.37354647]
  [0.06869823 0.08594641 0.72958382]
  [0.18604236 0.33659305 0.37461065]]

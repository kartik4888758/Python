import matplotlib.pyplot as plt

def matplotlib_example():
    # Sample data
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    # Plotting a simple line graph
    plt.plot(x, y, label='Linear Function')

    # Adding labels and title
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Simple Line Graph')

    # Adding a legend
    plt.legend()

    # Display the plot
    plt.show()

if __name__ == "__main__":
    matplotlib_example()

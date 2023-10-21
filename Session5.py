import math

# Define the main function
def main():
    # Number of data points
    num_points = 1000

    # Generate and print the table header
    print("x\t\tsin(x)")

    # Generate the table of sin(x) vs. x
    for i in range(num_points):
        x = 2 * i / (num_points - 1)  # Generate x values between 0 and 2
        sin_x = math.sin(x)  # Calculate sin(x)
        print(f"{x:.4f}\t\t{sin_x:.4f}")

if __name__ == "__main__":
    main()
def calculate_square_root(number):
    # Check for negative numbers
    if number < 0:
        return None  # Indicate error for negative numbers

    guess = number / 2.0  # Initial guess

    # Iterate to improve the guess
    for _ in range(10):
        guess = 0.5 * (guess + number / guess)

    return guess


def main():
    # Input: Get the number from the user
    number = float(input("Enter a number: "))

    # Calculate square root
    square_root = calculate_square_root(number)

    # Output: Display the result
    if square_root is not None:
        print(f"Square root of {number:.2f} is {square_root:.5f}")
    else:
        print("Cannot calculate square root of a negative number.")


if __name__ == "__main__":
    main()

def digit_root(num):
    """Calculates the digital root of a number."""
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num

# Input from the user
try:
    number = int(input("Enter a number: "))
    if number < 0:
        print("Please enter a positive number.")
    else:
        result = digit_root(number)
        print(f"The single-digit sum of {number} is {result}.")
except ValueError:
    print("Please enter a valid integer.")
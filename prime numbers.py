def is_prime(num):
    
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes(start, end):
    
    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=' ')
    print()

# Input from the user
try:
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))
    
    if start > end:
        print("Starting number should be less than or equal to the ending number.")
    else:
        print_primes(start, end)

except ValueError:
    print("Please enter valid integers.")
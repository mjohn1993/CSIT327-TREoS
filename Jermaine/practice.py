def gcd(a, b):
    while b:
        a, b = b, a % b  # Update a and b with the remainder
    return a

# Get user input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate and display the GCD
result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")

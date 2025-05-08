# Program to perform basic arithmetic operations

# Taking input from the user
a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

# Performing arithmetic operations
addition = a + b
subtraction = a - b
multiplication = a * b

# Handling division by zero
if b != 0:
    division = a / b
else:
    division = "Undefined (cannot divide by zero)"

# Displaying the results
print("\nResults:")
print("Addition       :", addition)
print("Subtraction    :", subtraction)
print("Multiplication :", multiplication)
print("Division       :", division)

# Demonstration of Python data types

# Integer variable
age = 22
# Float variable
height = 5.9
# String variable
name = "Abraar"
# Boolean variable
is_intern = True
# Printing values and their data types
print("Age:", age, "| Type:", type(age))
print("Height:", height, "| Type:", type(height))
print("Name:", name, "| Type:", type(name))
print("Is Intern:", is_intern, "| Type:", type(is_intern))

print("\n--- Arithmetic Operations ---")

# Arithmetic operations using numeric variables
sum_result = age + 5
product_result = age * 2
division_result = height / 2

print("Sum:", sum_result)
print("Product:", product_result)
print("Division:", division_result)

print("\n--- Type Casting with User Input ---")

try:
    # Taking input as string (default behavior of input())
    user_age = input("Enter your age: ")

    # Converting string input to integer
    user_age_int = int(user_age)

    # Converting string input to float
    user_age_float = float(user_age)

    print("Integer value:", user_age_int)
    print("Float value:", user_age_float)

except ValueError:
    # Handles invalid input like alphabets or symbols
    print("Invalid input! Please enter a numeric value.")

print("\n--- String Concatenation ---")

# Proper concatenation using type conversion
message = "My age is " + str(age)
print(message)

print("\n--- Dynamic Typing Demonstration ---")

# Variable initially holds integer
value = 10
print("Value:", value, "| Type:", type(value))

# Reassigning variable to string
value = "Now I am a string"
print("Value:", value, "| Type:", type(value))

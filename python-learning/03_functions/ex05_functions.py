# Exercise 05 - Functions
# -----------------------------------------
# GOAL: Package reusable code into named blocks you can call multiple times.
#
# CONCEPTS:
#   def name(parameters):  - defines a function
#   return value           - sends a result back to the caller
#   parameters             - inputs the function expects
#   arguments              - actual values passed when calling
#   default parameters     - a fallback value used when argument is not provided

# ------ YOUR PLAYGROUND BELOW ------

# 1. Basic function - no input, no output
def greet():
    print("Hello! Welcome to Python.")

greet()   # calling the function
greet()   # call it as many times as you like


# 2. Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Ajay")
greet_person("Alice")


# 3. Function that returns a value
def add(a, b):
    return a + b

result = add(3, 5)
print(f"3 + 5 = {result}")
print(f"10 + 20 = {add(10, 20)}")   # use the return value directly


# 4. Default parameter - used when caller doesn't provide it
def power(base, exponent=2):
    return base ** exponent

print(power(3))       # uses default exponent=2 → 9
print(power(3, 3))    # overrides default → 27


# 5. Multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([4, 1, 9, 2, 7])
print(f"Lowest: {low}, Highest: {high}")


# 6. Functions calling other functions
def square(n):
    return n * n

def sum_of_squares(a, b):
    return square(a) + square(b)

print(f"Sum of squares of 3 and 4: {sum_of_squares(3, 4)}")   # 9 + 16 = 25


# ------ CHALLENGES ------
# A) Write a function `is_even(n)` that returns True if n is even, False otherwise.
#    Test it with a few numbers using print().
#
# B) Write a function `celsius_to_fahrenheit(c)` that converts Celsius to Fahrenheit.
#    Formula: F = (C * 9/5) + 32
#    Ask the user for a temperature and print the converted value.
#
# C) Write a function `count_vowels(text)` that counts how many vowels
#    (a, e, i, o, u) are in a string (case-insensitive).
#    Hint: loop over each character and check if it is in "aeiou".

# Exercise 03 - Conditions (if / elif / else)
# -----------------------------------------
# GOAL: Make the program do different things based on a value.
#
# CONCEPTS:
#   if condition:    - runs the block if condition is True
#   elif condition:  - checked only when the previous if was False
#   else:            - runs when none of the above matched
#
#   Comparison operators:
#     ==   equal to
#     !=   not equal to
#     >    greater than
#     <    less than
#     >=   greater than or equal to
#     <=   less than or equal to
#
#   Logical operators:
#     and  - both conditions must be True
#     or   - at least one must be True
#     not  - flips True to False and vice versa
#
# IMPORTANT: Python uses INDENTATION (spaces/tab) to define blocks.
#            Everything indented under an if belongs to that if.

# ------ YOUR PLAYGROUND BELOW -----

# 1. Basic if/elif/else
age = int(input("Enter your age: "))

if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")

# 2. Combining conditions with and / or
score = int(input("Enter a test score (0-100): "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")

if score >= 60:
    print("You passed!")
else:
    print("You did not pass.")

# 3. and / or
temperature = int(input("What is the temperature outside (°C)? "))
is_raining = input("Is it raining? (yes/no) ").strip().lower()

if temperature > 20 and is_raining == "no":
    print("Great day to go outside!")
elif temperature > 20 and is_raining == "yes":
    print("Warm but rainy - bring an umbrella.")
elif temperature <= 20 and is_raining == "no":
    print("Cool day - wear a jacket.")
else:
    print("Cold and rainy - stay inside!")

# ------ CHALLENGES ------
# A) Ask the user to type a number. Print "even" if it is divisible by 2,
#    "odd" otherwise. Hint: the % operator gives you the remainder (e.g. 7 % 2 == 1).
# B) Ask for a password. If it equals "secret123" print "Access granted",
#    otherwise print "Wrong password".
# C) Ask for two numbers and print which one is larger, or "They are equal"
#    if both are the same.

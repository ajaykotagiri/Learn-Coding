# Exercise 04 - Loops (for / while)
# -----------------------------------------
# GOAL: Repeat actions without copy-pasting code.
#
# CONCEPTS:
#   for x in something:  - loops over each item in a sequence
#   range(n)             - generates numbers 0, 1, 2, ... n-1
#   range(start, stop)   - generates start, start+1, ... stop-1
#   range(start,stop,step) - jumps by step each time
#   while condition:     - keeps looping as long as condition is True
#   break                - immediately exits the loop
#   continue             - skips the rest of this iteration, goes to next

# ------ YOUR PLAYGROUND BELOW ------

# 1. for loop with range
print("--- Counting to 5 ---")
for i in range(1, 6):
    print(i)

# 2. Looping over a string (strings are sequences of characters)
print("--- Letters in your name ---")
name = "Ajay"
for letter in name:
    print(letter)

# 3. while loop - keeps going until a condition is False
print("--- Countdown ---")
count = 5
while count > 0:
    print(count)
    count -= 1       # same as: count = count - 1
print("Blast off!")

# 4. while with break - useful when you don't know how many iterations you need
print("--- Guess the number ---")
secret = 7
while True:
    guess = int(input("Guess the number (1-10): "))
    if guess == secret:
        print("Correct!")
        break
    elif guess < secret:
        print("Too low, try again.")
    else:
        print("Too high, try again.")

# 5. continue - skip even numbers, only print odd
print("--- Odd numbers from 1 to 10 ---")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

# ------ CHALLENGES ------
# A) Print the multiplication table for a number the user enters.
#    Example for 3:  3x1=3  3x2=6  ... 3x10=30
# B) Ask the user to keep entering words until they type "quit".
#    Count how many words they entered (not counting "quit") and print the total.
# C) Print all numbers from 1 to 50 that are divisible by both 3 and 5.
#    Hint: use `and` inside the if condition.

input("Press Enter to see the solutions...")    
# ------ SOLUTIONS ------
# A) Multiplication table
number = int(input("Enter a number to see its multiplication table: "))
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}") 

# B) Word counting
word_count = 0
while True:
    word = input("Enter a word (or type 'quit' to stop): ")
    if word.lower() == "quit":
        break
    word_count += 1
print(f"You entered {word_count} words.")   
# C) Divisible by 3 and 5
print("Numbers from 1 to 50 that are divisible by both 3 and 5:")
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print(i)        

        

# Exercise 02 - User Input & Strings
# -----------------------------------------
# GOAL: Read input from the user and manipulate text.
#
# CONCEPTS:
#   input()    - pauses the program and waits for the user to type something
#   int()      - converts text to a whole number
#   f-strings  - a clean way to embed variables inside text  f"Hello {name}"
#   str methods:
#     .upper()       - "hello" -> "HELLO"
#     .lower()       - "HELLO" -> "hello"
#     .strip()       - removes leading/trailing spaces
#     .replace(a, b) - replaces all occurrences of a with b
#     len()          - number of characters in a string

# ------ YOUR PLAYGROUND BELOW ------

# 1. Ask the user for their name
fname = input("What is your first name? ")
lname = input("What is your last name? ")
name = f"{lname}, {fname}"
print(f"Hello, {name}!")

# 2. Ask for age and do math with it (input() always returns text, so convert it)
age = int(input("How old are you? "))
print(f"In 5 years you will be {age + 5} years old.")

# 3. String methods
sentence = input("Type a sentence with extra spaces: " )
count = len(sentence)
print(count)                    # shows the original sentence with spaces
print(sentence.strip())               # removes extra spaces
print(sentence.strip().upper())       # ALL CAPS
print(sentence.strip().replace(" ", "_"))  # replaces spaces with underscores

# 4. len() counts characters
word = input("Type any word: ")
print(f'"{word}" has {len(word)} characters.')
print(f"Uppercase version: {word.upper()}")
print(f"First character: {word[0]}")

# ------ CHALLENGES ------
# A) Ask for the user's first and last name separately,
#    then print them combined as "Last, First" (e.g. "Kumar, Ajay").
# B) Ask for a sentence, then print how many characters it has
#    and the sentence with every space replaced by an underscore (_).
# C) Print the first character of the word the user typed above.
#    Hint: strings can be indexed like word[0]

# -------------------------------------------
# Exercise 1: Review - Variables, Input & Operators
# -------------------------------------------
# In this exercise, you’ll work in groups of 2–3.
# You’ll review how to:
# - Store and use variables
# - Use input() and print()
# - Apply arithmetic and comparison operators
#
# Each learner will build on the previous one’s work.
# This means you’ll use and extend each other’s variables.
#
# -------------------------------------------
# GROUP INSTRUCTIONS
# -------------------------------------------
# Work in groups of 2–3 learners.
# You will all share the same GitHub Classroom repository.
#
# After each task:
# - The learner who is currently coding will git add, commit, and push.
# - The next learner will move to their own computer, git pull, and continue.
#
# If you are in pairs:
# - Swap computers after each task (back and forth).
# -------------------------------------------


# Task 1: Storing and Printing Variables
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 1: Storing and Printing Variables\n"
    + "-------------------------------------------")
# TODO:
# 1. Create two variables: name and age.
# 2. Ask the user for their name and age using input().
# 3. Print a message that says: "Hello <name>, you are <age> years old."
#
# Example:
# Enter your name: Sam
# Enter your age: 30
# Output: Hello Sam, you are 30 years old.
#
# Write your code below:


# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# 1. Save your file
# 2. Open the terminal
# 3. Run:
#    git add Ex1_review.py
#    git commit -m "Completed Task 1 - user name and age"
#    git push origin main
# 4. The next learner goes to their own computer.
# 5. On their computer, open the terminal and run:
#    git pull
# -------------------------------------------


# Task 2: Arithmetic Practice
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 2: Arithmetic Practice\n"
    + "-------------------------------------------")
# You will now use the variable 'age' from the previous task.
# You DO NOT need to create a new 'age' variable.
#
# TODO:
# 1. Create a new variable called 'next_year_age' and set it to age + 1.
# 2. Print a message like: "Next year, you will be <next_year_age> years old."
# 3. Create another variable called 'decades' which is age divided by 10.
# 4. Print: "That means you are about <decades> decades old!"
#
# Example:
# Output:
# Next year, you will be 31 years old.
# That means you are about 3.1 decades old.
#
# Write your code below:


# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# 1. Save and push:
#    git add Ex1_review.py
#    git commit -m "Completed Task 2 - arithmetic practice"
#    git push origin main
# 2. Next learner: git pull
# -------------------------------------------


# Task 3: Comparison Operators
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 3: Comparison Operators\n"
    + "-------------------------------------------")
# You will now compare the user's age using if-statements.
#
# TODO:
# 1. Use if, elif, else to print:
#    - "You are a Boomer!" if age is between 61 and 79 (inclusive)
#    - "You are Gen X!" if age is between 45 and 60 (inclusive)
#    - "You are a Millenial!" if age is between 29 and 44 (inclusive)
#    - "You are not a Boomer, Millenial or Gen X" otherwise.
#
# Example:
# Output:
# You are an adult!
#
# Write your code below:


# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# 1. Save and push:
#    git add Ex1_review.py
#    git commit -m "Completed Task 3 - comparison operators"
#    git push origin main
# 2. Next learner: git pull
# -------------------------------------------


# Task 4: Combining Variables and Operators
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 4: Combining Variables and Operators\n"
    + "-------------------------------------------")
# Let’s combine what we’ve learned.
#
# TODO:
# 1. Create a variable 'year_of_birth' using the current year (2025) minus their age.
# 2. Print: "You were born in <year_of_birth>."
# 3. If the year_of_birth is before 2000, print "You were born in the 20th century!"
#    Otherwise, print "You were born in the 21st century!"
#
# Example:
# Output:
# You were born in 2005.
# You were born in the 21st century!
#
# Write your code below:


# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# 1. Save and push:
#    git add Ex1_review.py
#    git commit -m "Completed Task 4 - combining operators"
#    git push origin main
# 2. Next learner: git pull
# -------------------------------------------


# Task 5: Mini Challenge
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 5: Mini Challenge\n"
    + "-------------------------------------------")
# Build a short interactive summary program.
#
# TODO:
# 1. Reuse all the variables created so far.
# 2. Print a final summary message like:
#    "Hello <name>! You are <age> years old, born in <year_of_birth>.
#     Next year you will be <next_year_age>. That’s about <decades> decades old!"
#
# Write your code below:


# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# 1. Save and push:
#    git add Ex1_review.py
#    git commit -m "Completed Task 5 - final review summary"
#    git push origin main
# 2. Next learner: git pull
# -------------------------------------------


# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------
# Once all learners have had a turn, continue swapping computers
# for each extension as before.
# -------------------------------------------

# Extension 1:
# -------------------------------------------
print("-------------------------------------------\n"
    + "Extension 1:\n"
    + "-------------------------------------------")
# Ask the user for their favourite number.
# Multiply it by their age and print the result.
# Example:
# Enter your favourite number: 3
# Output:
# Your lucky total is 54!

# Write your code below:


# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# 1. Save and push:
#    git add Ex1_review.py
#    git commit -m "Completed Extension 1 - favourite number"
#    git push origin main
# 2. Next learner: git pull
# -------------------------------------------


# Extension 2:
# -------------------------------------------
print("-------------------------------------------\n"
    + "Extension 2:\n"
    + "-------------------------------------------")
# Create a small comparison:
# Ask the user for another person's age.
# Compare it to the original age and print:
# - "<name> is older than <other_name>"
# - "<name> is younger than <other_name>"
# - "<name> and <other_name> are the same age!"
#
# Write your code below:


# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# 1. Save and push:
#    git add Ex1_review.py
#    git commit -m "Completed Extension 2 - age comparison"
#    git push origin main
# 2. Next learner: git pull
# -------------------------------------------


# -------------------------------------------
# ADVANCED ACTIVITY
# -------------------------------------------
print("-------------------------------------------\n"
    + "ADVANCED ACTIVITY\n"
    + "-------------------------------------------")
# Choose one learner’s computer to finish this challenge.
#
# Advanced Task:
# Create a simple “age calculator” program that:
# 1. Asks for the user's name and year of birth.
# 2. Calculates their age automatically.
# 3. Tells them whether they are an adult, teenager, or child.
# 4. Prints a final message: "Hello <name>, you are <age> years old in 2025!"
#
# Hint: Use subtraction (2025 - year_of_birth).
#
# Write your code below:


# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# Once you’ve completed this exercise:
# 1. Save your file
# 2. Open the terminal
# 3. Run:
#    git add Ex1_review.py
#    git commit -m "Completed advanced review activity"
#    git push origin main
# 4. Check GitHub to confirm your group’s final version appears.
# -------------------------------------------

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
name = input("What is your name?: ")
age = int(input("What is your age?: "))
print(f" Hello {name}, you are {age} years old.")
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
next_year_age = age + 1
print(f"Next year, you will be {next_year_age} years old")
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
if age >= 61 and age <=79:
    print ("You are a boomer!")
elif age >= 45 and age <=60:
    print ("You are Gen X!")
elif age >= 29 and age <= 44:
    print ("You are Millenial!")
else:
    print ("You are not a Boomer, Millenial or Gen X")
    

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
year_of_birth= 2025 - age
print(f"You were born in {year_of_birth}. ")
if year_of_birth < 2000:
    print("You were born in the 20th century!!")
else:
    print("You were born in the 21st century! ")
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
decades = age / 10
print(f"Hello {name}! You are {age} years old, born in {year_of_birth}.")
print(f"Next year you will be {next_year_age}. That's about {decades} decades old!")
# -------------------------------------------
# SWAP COMPRS
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
favourite_number = int(input("What is your favourite number?: "))
lucky_total = favourite_number * age 
print(f"your lucky total is {lucky_total}! ")
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
person2_name = input("Enter person 2 name: ")
person2_age = int(input(f"Enter {person2_name}'s age: "))
if age > person2_age:
    print(f"{name} is older than {person2_name}.") 
elif age < person2_age:
    print(f"{name} is younger than {person2_name}.")
else:
    print(f"{name} and {person2_name} are the same age!")
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
user_name = input("What is your name?: ")
year_of_birth = int(input("What year were you born?: "))
age = 2025 - year_of_birth
if age >= 18: 
    print(f"You are an adult!")
elif age >= 13:
    print(f"You are a teenager.")
else:
    print(f"You are a child!")
print(f"Hello {user_name}, you are {age} years old in 2025!")

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




tasks = []
print(tasks)


print(f"=================================================================")
print(f"TASK MANAGER SYSTEM")
print(f"Keep track of your daily tasks")
print(f"=================================================================")
print()


print()
choice = "0"
while choice != "5":
        print()
        print("1. Add task")
        print("2. View all tasks")
        print("3. Search for tasks")
        print("4. View statistics")
        print("5. Exit")
        print()
        choice = input("Select an option: ")
        print()
        while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
            print("ERROR: Invalid choice")
            print()
            print("1. Add task")
            print("2. View all tasks")
            print("3. Search for tasks")
            print("4. View statistics")
            print("5. Exit")
            print()
            choice = input("Select an option: ") 
        if choice == "1":
            task_name = input("Enter task name: ")
            while task_name == "":
                 print("ERROR: Task name cannot be blank")
                 task_name = input("Enter task name: ")
            priority = input("Enter priority (High/Medium/Low): ")
            while priority == "":
                 print("ERROR: Priority cannot be blank")
                 priority = input("Enter priority (High/Medium/Low): ")              
            print()
            task = {
                 "name": task_name,
                 "priority": priority,
                 "status": "Not started"
            }
            tasks.append(task)
            print("Task added successfully")
            print()
        elif choice == "2":
          if len(tasks) == 0:
               print("No tasks recorded yet")
               print()
        elif choice == "3":
               if len(tasks) == 0:
                    print("No tasks to search")
                    print()
               else:
                    search_name = input("Enter task name to search for: ")
                    found = False
                    for task in tasks:
                         if task["name"] == search_name:
                              print()
                              print("Task found:")
                              print(f"Name: {task['name']}")
                              print(f"Priority: {task['priority']}")
                              print(f"Status: {task['status']}")
                              print()
                              found = True
                    if found == False:
                      print()
                      print("No matching tasks found")
                      print()
        elif choice == "4":
               if len(tasks) == 0:
                    print("No tasks to calculate statistics")
                    print()
               else:
                    high_count = 0
                    medium_count = 0
                    low_count = 0
                    for task in tasks:
                        if task["priority"] == "High":
                            high_count = high_count + 1
                        elif task["priority"] == "Medium":
                            medium_count = medium_count + 1
                        elif task["priority"] == "Low":
                            low_count = low_count + 1
                    print("Task Statistics:")
                    print(f"Total tasks: {len(tasks)}")
                    print(f"High priority: {high_count}")
                    print(f"Medium priority: {medium_count}")
                    print(f"Low priority: {low_count}")
                    print()
        elif choice == "5":
            print("Thank you for using the Task Manager")
            print("Goodbye")    
        else:
               print("All tasks:")
               print()
               for task in tasks:
                    print(f"Name: {task['name']}")
                    print(f"Priority: {task['priority']}")
                    print(f"Status: {task['status']}")
                    print("---------------------------------------")
               print()

# -------------------------------------------
# Assessment 3: Library Book Tracker
# Manchester Central Library (Brief 5)
# -------------------------------------------
# Think carefully about how to structure your code, validate user input,
# and present information clearly to the user.
#
# Remember to save, stage, commit, and push after completing each task.
# -------------------------------------------

# -------------------------------------------
# TODO
# -------------------------------------------
# 1. Delete the other briefs' Python files inside this repository.
# 2. Rename this file to your own program's name (e.g. tax_calculator.py)
# 3. Run:
#    git add .
#    git commit -m "Started project"
#    git push origin main
# -------------------------------------------


# -------------------------------------------
# Task 1: Data Storage
# -------------------------------------------
# Decide how to store all book loan records.
# Each record should contain key details about the book and the borrower.
# Choose a suitable data structure and initialise it clearly.
#
# Commit your progress after completing this task.

# Your code here:


# -------------------------------------------
# Task 2: Welcome Message
# -------------------------------------------
# Display a clear and professional welcome message for library staff.
# Make it obvious what the system is for and who it’s intended to help.
#
# Commit your progress after completing this task.

# Your code here:



# -------------------------------------------
# Task 3: Main Menu
# -------------------------------------------
# Design a main menu that allows staff to interact with the system.
# Include options such as:
# - Record a new book loan
# - View all borrowed books
# - Exit the program
#
# The menu should continue to display until the staff member exits.
# Handle invalid input gracefully.
#
# Commit your progress after completing this task.

# Your code here:


# -------------------------------------------
# Task 4: Record a Book Loan
# -------------------------------------------
# Allow staff to enter details for a new loan, such as:
# - Book title
# - Author
# - Borrower’s name
#
# Validate all inputs (no blanks or invalid entries).
# Store each record in your main data structure.
# Display a confirmation message once the loan has been recorded successfully.
#
# Commit your progress after completing this task.

# Your code here:





# -------------------------------------------
# Task 5: View All Borrowed Books
# -------------------------------------------
# Display a neatly formatted list of all current book loans.
# Include all relevant details and ensure the display is easy to read.
# Consider numbering each loan for clarity.
# Ensure the program handles the case where no books have been borrowed yet.
#
# Commit your progress after completing this task.

# Your code here:



# -------------------------------------------
# Task 6: Exit and Error Handling
# -------------------------------------------
# Add an option to exit the program with a polite goodbye message.
# Handle any invalid menu selections without crashing.
#
# Commit your progress after completing this task.

# Your code here:



# -------------------------------------------
# Task 7: Testing and Comments
# -------------------------------------------
# Test your program thoroughly:
# - Record multiple book loans
# - Try blank inputs to check validation
# - View records when none exist
# - Test invalid menu selections
#
# Add clear comments throughout your code.
# Follow Python naming conventions and check for tidy, professional output.
#
# Commit your final version when finished.
# -------------------------------------------


# -------------------------------------------
# Extension Ideas (Optional)
# -------------------------------------------
# If you finish early, you could:
# - Add due dates for returns
# - Search for books by title or borrower name
# - Mark books as returned
# - Track overdue books
# - Include book categories or genres
# -------------------------------------------













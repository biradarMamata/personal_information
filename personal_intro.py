# Personal Introduction Program
# Week 1 - Python Basics

print("=" * 45)
print("        PERSONAL INTRODUCTION")
print("=" * 45)

 #Getting user input for personal information
name = input("What is your name? ")
age = int(input("How old are you? "))
city = input("Which city are you from? ")
hobby = input("What is your favorite hobby? ")

# Getting user input for favorite foods
food1 = input("What is your favorite food? ")
food2 = input("What is another food you like? ")
food3 = input("What is one more food you enjoy? ")

# Here storing the favorite foods in a list for easy access which i got from the user
favorite_foods = [food1, food2, food3]

print("\n--- Your Profile ---")

# Displaying the collected information back to the user using f-strings for better readability
print(f"Name   : {name}")
print(f"Age    : {age}")
print(f"City   : {city}")
print(f"Hobby  : {hobby}")

# Calculating the user's age next year and displaying it using basic arithmetic and f-strings
next_year_age = age + 1
print(f"Next year, you will be {next_year_age} years old.")

# Displaying the favorite foods by acssessing the list elements using indexing and f-strings
print("\n--- Favorite Foods ---")
print(f" 1. {favorite_foods[0]}")
print(f" 2. {favorite_foods[1]}")
print(f"3. {favorite_foods[2]}")

# Creating a personalized welcome message using string concatenation and displaying it to the user
welcome_message = "Nice to meet you, " + name + "!"
print(welcome_message + " I hope you have a great day.")

print("\nThank you for introducing yourself!")
print("Keep learning and keep coding!")
print("=" * 45)
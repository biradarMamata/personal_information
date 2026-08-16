#  Personal Introduction Program

## Project Overview

The Personal Introduction Program is a simple Python program created as part of Week 1 Python Basics practice.

The program asks the user for some basic information such as their name, age, hobby, and city. It then uses the entered information to display a friendly and personalized welcome message.

The main goal of this project is to practice the basic Python concepts learned during the first week, including variables, strings, input, output, lists, basic mathematical operations, and f-strings.

---

## What I Learned

During this project, I practiced the following Python concepts:

* How to create and run a Python program
* How to use `print()` to display information
* How to use `input()` to get information from the user
* How to store information in variables
* Working with strings
* Using f-strings to create personalized messages
* Creating and accessing lists
* Performing simple mathematical operations
* Adding comments to make code easier to understand
* Testing a program with different inputs and checking the output

This project helped me understand how Python code takes input from a user, processes the information, and produces an output.

---

## Features

The program:

* Asks the user's name
* Asks the user's age
* Asks the user's favorite hobby
* Asks the user's city
* Stores the information using variables
* Calculates the user's age next year
* Uses a list to store favorite foods
* Displays a friendly personalized message

---

## Setup Instructions

### 1. Install Python

Download and install Python 3 from the official Python website.

During installation, make sure Python is added to the system PATH.

### 2. Check Python Installation

Open PowerShell or Command Prompt and run:

```bash
py --version
```

The installed Python version should be displayed.

### 3. Clone or Download the Project

Download this project and open the project folder.

### 4. Open the Project

Open the `personal inf` folder in VS Code or another code editor.

### 5. Run the Program

Open the terminal inside the project folder and run:

```bash
py personal_intro.py
```

### 6. Enter the Information

The program will ask for your name, age, hobby, and city.

Enter the requested information and the program will display your personalized introduction.

---

## Code Structure

The project is kept simple because it is a beginner-level Python project.

```text
personal inf/
│
├── personal_intro.py
├── README.md
├── requirements.txt
└── screenshot.png
```

### File Description

| File                | Purpose                                                |
| ------------------- | ------------------------------------------------------ |
| `personal_intro.py` | Contains the main Python program                       |
| `README.md`         | Contains project documentation                         |
| `requirements.txt`  | Lists external Python packages required by the project |
| `screenshot.png`    | Shows the program running successfully                 |

---

## Technical Details

### Variables

Variables are used to store the information entered by the user.

Examples:

```python
name = input("What is your name? ")
age = int(input("How old are you? "))
hobby = input("What is your favorite hobby? ")
city = input("Which city do you live in? ")
```

### Input

The `input()` function is used to get information from the user.

```python
name = input("What is your name? ")
```

### Strings

The program works with text such as the user's name, hobby, and city.

### List

A list is used to store multiple favorite foods:

```python
favorite_foods = ["Biryani", "Pizza", "Dosa"]
```

An item from the list can be accessed using its index:

```python
favorite_foods[0]
```

### Basic Mathematical Operation

The program performs a simple calculation to find the user's age next year:

```python
next_year = age + 1
```

### F-Strings

F-strings are used to display personalized information:

```python
print(f"You are {age} years old.")
```

### Algorithm

The program follows a simple sequence:

```text
Start
  ↓
Ask for user's information
  ↓
Store information in variables
  ↓
Perform a simple calculation
  ↓
Access information from the list
  ↓
Display personalized welcome message
  ↓
End
```

There is no complex algorithm because this is a basic introductory project. The program mainly follows a sequential flow.

### Data Structures

The main data structure used is a list.

python
favorite_foods = ["Biryani", "Pizza", "Dosa"]

Variables are also used to store individual pieces of information such as the user's name, age, hobby, and city.

### Architecture

The project uses a simple single-file structure.

The program follows:

Input → Processing → Output

Input: User enters personal information.
Processing: The program stores the information and calculates the next year's age.
Output: The program displays the personalized introduction.



## Visual Documentation

The program was tested by running it through the terminal.

### Sample Output

text
Welcome to my Personal Introduction Program!
---------------------------------------------
What is your name? Mamata
How old are you? 19
What is your favorite hobby? Coding
Which city do you live in? Bengaluru

 Welcome, Mamata! 
It's nice to know a little about you.

Your name is Mamata.
You are 19 years old.
You enjoy Coding.
You are from Bengaluru.
Next year, you will be 20 years old.
One of my favorite foods is Biryani.

Thanks for introducing yourself! 😊


A screenshot of the actual program execution is included in the project as:

text
screenshot.png

## Testing Evidence

The program was tested using different inputs to make sure that the information entered by the user was displayed correctly.

### Test Case 1 — Normal Input

Input:

text
Name: Mamata
Age: 19
Hobby: Coding
City: Bengaluru

Expected Result:

The program should display the entered information and calculate the next year's age as 20.

Result: Passed


### Test Case 2 — Different User Information

Input:

text
Name: Alex
Age: 21
Hobby: Reading
City: Mumbai


Expected Result:

The program should display Alex's information and calculate the next year's age as 22.

Result: Passed

---

### Test Case 3 — Different Hobby and City

Input:

text 
 Name: Rahul
 Age: 18
 Hobby: Cricket
 City: Pune


Expected Result:

The program should display the entered information and calculate the next year's age as 19.

Result: Passed

## Validation

The following features were checked during testing:

*  Program runs successfully
*  User can enter their name
*  User can enter their age
*  User can enter their hobby
*  User can enter their city
*  Information is stored in variables
*  List is created and accessed
*  Age calculation works correctly
*  Personalized output is displayed
*  Program works with different inputs

---

## Conclusion

This project gave me practical experience with the basic Python concepts covered during Week 1. I learned how to take input from users, store information in variables, work with strings and lists, perform simple calculations, and display personalized output.

Although the project is simple, it helped me understand the basic flow of a Python program from taking input to processing information and displaying the result.


# 🧮 Python Calculator

A **simple beginner-friendly calculator** program written in Python.  
This project allows users to perform basic arithmetic operations using user input — ideal for learning Python fundamentals like conditionals, data types, and input handling.

---

## 📘 Overview

This calculator performs **Addition (+)**, **Subtraction (-)**, **Multiplication (*)**, and **Division (/)**.  
It takes user input for the operator and two numbers, then prints the calculated result.

---

## ⚙️ Features

✅ Supports four basic operations:  
- Addition (`+`)  
- Subtraction (`-`)  
- Multiplication (`*`)  
- Division (`/`)  

🚫 Handles invalid operator input gracefully  
💬 Provides clear, readable output for beginners  

---

## 🧠 How It Works

1. The program asks the user to **enter an operator** (`+`, `-`, `*`, or `/`).  
2. The user is prompted to enter **two numbers**.  
3. The program performs the chosen arithmetic operation.  
4. The **result is displayed**.  
5. If the operator is invalid, an error message is shown.

---

## 💻 Code Example

```python
# Python Calculator program
# a simple beginner friendly program

operator = input("Enter a operator /,+ , * , - :")
num1 = float(input("Enter the first number :"))
num2 = float(input("Enter the second number :"))

if operator == "+":
    result = num1 + num2
    print("Result =", result)
elif operator == "-":
    result = num1 - num2
    print("Result =", result)
elif operator == "/":
    result = num1 / num2
    print("Result =", result)
elif operator == "*":
    result = num1 * num2
    print("Result =", result)
else:
    print(f"This {operator} is not a valid operator")
# A simple Python Calculator

This is a simple fun **Python Calculator** 

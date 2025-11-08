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


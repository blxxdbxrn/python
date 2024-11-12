import math

operator = input("What is your operator?(+ - * /):")
num1 = float(input("What is your first number?"))
num2 = float(input("What is your second number?"))

if operator == "+":
    result = num1 + num2
    print(f"Result is: {result}!")
elif operator == "-":
    result = num1 - num2
    print(f"Result is {result}!")
elif operator == "*":
    result = round(num1 * num2, 2)
    print(f"Result is: {result}!")
elif operator == "/":
    result = round(num1 / num2, 2)
    print(f"Result is: {result}!")
else:
    print(f"Invalid operator '{operator}'!")

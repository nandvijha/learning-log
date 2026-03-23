#Python Calculator
operator = input("Enter your operator (+ - * / %): ")
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

# print(num1 + num2)

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} is invalid operator")

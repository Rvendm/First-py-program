

# Mag ask at mag-aaccept ng user input
operator = input("Enter an operator (+ - * /): ")

# variable num1 nagassign ng user input
num1 = float(input("Enter the 1st number: "))
# variable num2 nagassign ng user input
num2 = float(input("Enter the 2nd number: "))


if operator == "+":  # if condition, dito magsimula ang logic para sa condition ng operators na napili
    result = num1 + num2
    print(round(result))
elif operator == "-":
    result = num1 - num2
    print(round(result))
elif operator == "*":
    result = num1 * num2
    print(round(result))
elif operator == "/":
    result = num1 / num2
    print(round(result))
else:
    # mag cacatch ng input if hindi operator ang na input
    print("Invalid Input!!!")

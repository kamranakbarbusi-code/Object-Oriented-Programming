number1 = int(input("Enter a number: "))
operator = input("Enter the operator: ")
number2 = int(input("Enter a number: "))

if operator == "+":
    c = number1 + number2
elif operator == "-":
    c = number1 - number2
elif operator == "*":
    c = number1 * number2
elif operator == "/":
    c = number1 / number2
print("Equals:", c)

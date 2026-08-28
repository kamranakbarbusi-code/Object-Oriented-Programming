number1 = int(input("Enter first number"))
number2 = int(input("Enter second number"))
number3 = int(input("Enter third number"))

if number1 > number2 and number1 > number3:
    print("Number1 the biggest")
elif number2 > number1 and number2 > number3:
    print("Number2 is the biggest")
elif number3 > number2 and number3 > number1:
    print("Number3 is the biggest")


if number1 < number2 and number1 < number3:
    print("Number1 the smallest")
elif number2 < number1 and number2 < number3:
    print("Number2 the smallest")
elif number3 < number1 and number3 < number2:
    print("Number3 the smallest")



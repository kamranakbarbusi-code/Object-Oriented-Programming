while (True):
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")
    print("5 Exit")
    choice = input("Enter your choice: ")
    if choice == "5":
        exit()

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == "1":
       print(a+b)

    elif choice == "2":
        print(a-b)

    elif choice == "3":
        print(a*b)

    elif choice == "4":
        print(a/b)





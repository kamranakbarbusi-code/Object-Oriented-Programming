while (True):
    print("1 Area of a Rectangle")
    print("2 Volumne of a Cube")
    print("3 Area of a Circle")
    print("4 Circumference of a Circle")
    print("5 Exit")
    choice = input("Enter your choice:")
    if choice == "5":
        exit()

    if choice == "1":
        length = int(input("Enter length:"))
        width = int(input("Enter width:"))
        print("The Area of the Rectangle is:", length*width)

    elif choice == "2":
        length = int(input("Enter length:"))
        width = int(input("Enter width:"))
        height = int(input("Enter height:"))
        print("The Volume of the Cube is:", length*width*height)

    elif choice == "3":
        radius = int(input("Enter the radius:"))
        print("The Area of the Circle is:", 3.14*radius*radius)

    elif choice == "4":
        radius = int(input("Enter radius:"))
        print("The Circumference of the Circle is:", 2*3.14*radius)
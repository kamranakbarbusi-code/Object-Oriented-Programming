StudentName = input("Enter Student Name: ")
Grade1 = int(input("Enter Course One Grade: "))
Grade2 = int(input("Enter Course Two Grade: "))
Grade3 = int(input("Enter Course Three Grade: "))

total = int (Grade1 + Grade2 + Grade3)
percentage = (total / 300) * 100


if percentage >= 90:
    print("Grade A")
elif percentage >= 80 and percentage <= 90:
    print("Grade B")
elif percentage >= 70 and percentage <= 80:
    print("Grade C")
elif percentage >= 60 and percentage <= 70:
    print("Grade D")



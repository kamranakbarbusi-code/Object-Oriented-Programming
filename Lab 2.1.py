i = 1

myEmployees = {}


def add_employee(i):
    name = input("Enter Employee Name: ")
    basicPay = int(input("Enter Basic Pay: "))
    allowance = int(input("Enter Allowance: "))
    deductions = int(input("Enter Deductions: "))
    taxes = int(input("Enter Taxes: "))

    grossPay = basicPay + allowance
    netPay = grossPay - deductions - taxes

    myEmployees["name" + str(i)] = {
        "name": name,
        "Basic Pay": basicPay,
        "Allowance": allowance,
        "Deductions": deductions,
        "Taxes": taxes,
        "Gross Pay": grossPay,
        "Net Pay": netPay
    }

    print("Employee Added")


def delete_employee():
    employee = int(input("Enter Employee Number to Delete: "))

    if "name" + str(employee) in myEmployees:
        del myEmployees["name" + str(employee)]
        print("Employee Deleted")

    else:
        print("Employee Not Found")


def modify_employee():
    employee = int(input("Enter Employee Number to Modify: "))

    if "name" + str(employee) in myEmployees:
        name = input("Enter Employee Name: ")
        basicPay = int(input("Enter Basic Pay: "))
        allowance = int(input("Enter Allowance: "))
        deductions = int(input("Enter Deductions: "))
        taxes = int(input("Enter Taxes: "))

        grossPay = basicPay + allowance
        netPay = grossPay - deductions - taxes

        myEmployees["name" + str(employee)]["name"] = name
        myEmployees["name" + str(employee)]["Basic Pay"] = basicPay
        myEmployees["name" + str(employee)]["Allowance"] = allowance
        myEmployees["name" + str(employee)]["Deductions"] = deductions
        myEmployees["name" + str(employee)]["Taxes"] = taxes
        myEmployees["name" + str(employee)]["Gross Pay"] = grossPay
        myEmployees["name" + str(employee)]["Net Pay"] = netPay

        print("Employee Modified")

    else:
        print("Employee Not Found")


def display_employees():
    for employee in myEmployees:
            print("Employee:", employee)
            print("Name:", myEmployees[employee]["name"])
            print("Basic Pay:", myEmployees[employee]["Basic Pay"])
            print("Allowance:", myEmployees[employee]["Allowance"])
            print("Deductions:", myEmployees[employee]["Deductions"])
            print("Taxes:", myEmployees[employee]["Taxes"])
            print("Gross Pay:", myEmployees[employee]["Gross Pay"])
            print("Net Pay:", myEmployees[employee]["Net Pay"])
            print("----------------------")


while True:
    print("Employee Payroll Management")
    print("1. Add an Employee")
    print("2. Delete an Employee")
    print("3. Modify an Employee")
    print("4. Display All Employees")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_employee(i)
        i = i + 1

    elif choice == 2:
        delete_employee()

    elif choice == 3:
        modify_employee()

    elif choice == 4:
        display_employees()

    elif choice == 5:
        break

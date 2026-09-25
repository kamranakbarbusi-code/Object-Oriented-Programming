myEmployees = {
    "John": {
        "Basic Pay": 3000,
        "Allowance": 500,
        "Deductions": 200,
        "Taxes": 300,
        "Gross Pay": 3500,
        "Net Pay": 3000
    }
}


def add_employee():
    name = input("Enter Employee Name: ")
    basicPay = int(input("Enter Basic Pay: "))
    allowance = int(input("Enter Allowance: "))
    deductions = int(input("Enter Deductions: "))
    taxes = int(input("Enter Taxes: "))

    grossPay = basicPay + allowance
    netPay = grossPay - deductions - taxes

    myEmployees[name] = {
        "Basic Pay": basicPay,
        "Allowance": allowance,
        "Deductions": deductions,
        "Taxes": taxes,
        "Gross Pay": grossPay,
        "Net Pay": netPay
    }
    print("Employee Added")


def delete_employee():
    name = input("Enter Employee Name to Delete: ")

    if name in myEmployees:
        del myEmployees[name]
        print("Employee Deleted")

    else:
        print("Employee Not Found")


def modify_employee():
    name = input("Enter Employee Name to Modify: ")

    if name in myEmployees:
        basicPay = int(input("Enter New Basic Pay: "))
        allowance = int(input("Enter New Allowance: "))
        deductions = int(input("Enter New Deductions: "))
        taxes = int(input("Enter New Taxes: "))

        grossPay = basicPay + allowance
        netPay = grossPay - deductions - taxes

        myEmployees[name]["Basic Pay"] = basicPay
        myEmployees[name]["Allowance"] = allowance
        myEmployees[name]["Deductions"] = deductions
        myEmployees[name]["Taxes"] = taxes
        myEmployees[name]["Gross Pay"] = grossPay
        myEmployees[name]["Net Pay"] = netPay

    else:
        print("Employee Not Found")


def display_employees():
    for name in myEmployees:
        print("Employee Name:", name)
        print("Basic Pay:", myEmployees[name]["Basic Pay"])
        print("Allowance:", myEmployees[name]["Allowance"])
        print("Deductions:", myEmployees[name]["Deductions"])
        print("Taxes:", myEmployees[name]["Taxes"])
        print("Gross Pay:", myEmployees[name]["Gross Pay"])
        print("Net Pay:", myEmployees[name]["Net Pay"])
        print()


while True:
    print("Employee Payroll")
    print("1. Add an Employee")
    print("2. Delete an Employee")
    print("3. Modify an Employee")
    print("4. Display All Employees")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_employee()

    elif choice == 2:
        delete_employee()

    elif choice == 3:
        modify_employee()

    elif choice == 4:
        display_employees()

    elif choice == 5:
        break

    else:
        print("Invalid Choice")
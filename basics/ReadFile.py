

employees_file = open("basics/employees.txt", "r")

if employees_file.readable():
    for employee in employees_file.readlines():
        print(employee)


employees_file.close()

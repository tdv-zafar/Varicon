# Task 1: Employee Management System (Console Based)
import json

# Employee Class
class Employee:

    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def to_dict(self):
        return {
            "id": self.emp_id,
            "name": self.name,
            "age": self.age,
            "salary": self.salary
        }


# Employee Manager Class
class EmployeeManager:

    def __init__(self, filename):
        self.filename = filename

    # Load employees from JSON
    def load_employees(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except:
            return []

    # Save employees to JSON
    def save_employees(self, employees):
        with open(self.filename, "w") as file:
            json.dump(employees, file, indent=4)

    # Add employee
    def add_employee(self):

        employees = self.load_employees()

        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = float(input("Enter Salary: "))

        emp = Employee(emp_id, name, age, salary)

        employees.append(emp.to_dict())

        self.save_employees(employees)

        print("Employee Added Successfully")

    # View employees
    def view_employees(self):

        employees = self.load_employees()

        if len(employees) == 0:
            print("No employees found")
            return

        print("\nEmployee List")

        for emp in employees:
            print("ID:", emp["id"])
            print("Name:", emp["name"])
            print("Age:", emp["age"])
            print("Salary:", emp["salary"])
            print("-------------------")

    # Delete employee
    def delete_employee(self):

        employees = self.load_employees()

        emp_id = int(input("Enter Employee ID to delete: "))

        new_list = []

        for emp in employees:
            if emp["id"] != emp_id:
                new_list.append(emp)

        self.save_employees(new_list)

        print("Employee Deleted")

    # Update employee
    def update_employee(self):

        employees = self.load_employees()

        emp_id = int(input("Enter Employee ID to update: "))

        for emp in employees:

            if emp["id"] == emp_id:

                emp["name"] = input("Enter New Name: ")
                emp["age"] = int(input("Enter New Age: "))
                emp["salary"] = float(input("Enter New Salary: "))

                print("Employee Updated")
                break

        self.save_employees(employees)


# Main Program
manager = EmployeeManager("employees.json")

while True:

    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        manager.add_employee()

    elif choice == "2":
        manager.view_employees()

    elif choice == "3":
        manager.update_employee()

    elif choice == "4":
        manager.delete_employee()

    elif choice == "5":
        print("Program Ended")
        break

    else:
        print("Invalid choice")
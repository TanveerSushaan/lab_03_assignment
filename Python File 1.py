class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp_id, name, age, salary):
        employee = Employee(emp_id, name, age, salary)
        self.employees.append(employee)

    def search_by_age(self, age):
        result = [emp for emp in self.employees if emp.age == age]
        return result

    def search_by_name(self, name):
        result = [emp for emp in self.employees if emp.name == name]
        return result

    def search_by_salary(self, operator, salary):
        operators = {
            ">": lambda x, y: x > y,
            "<": lambda x, y: x < y,
            ">=": lambda x, y: x >= y,
            "<=": lambda x, y: x <= y,
        }
        result = [emp for emp in self.employees if operators[operator](emp.salary, salary)]
        return result

    def print_results(self, results):
        if not results:
            print("No results found.")
        else:
            for emp in results:
                print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")

if __name__ == "__main__":
    employee_table = EmployeeTable()

    # Populate the Employee Table
    employee_table.add_employee("161E90", "Raman", 41, 56000)
    employee_table.add_employee("161F91", "Himadri", 38, 67500)
    employee_table.add_employee("161F99", "Jaya", 51, 82100)
    employee_table.add_employee("171E20", "Tejas", 30, 55000)
    employee_table.add_employee("171G30", "Ajay", 45, 44000)

    while True:
        print("\nSearch Options:")
        print("1. Search by Age")
        print("2. Search by Name")
        print("3. Search by Salary (>, <, <=, >=)")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            age = int(input("Enter age to search: "))
            results = employee_table.search_by_age(age)
            employee_table.print_results(results)
        elif choice == "2":
            name = input("Enter name to search: ")
            results = employee_table.search_by_name(name)
            employee_table.print_results(results)
        elif choice == "3":
            operator = input("Enter operator (>, <, <=, >=): ")
            salary = int(input("Enter salary to search: "))
            results = employee_table.search_by_salary(operator, salary)
            employee_table.print_results(results)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4).")



class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        return f"Name: {self.name}, ID: {self.employee_id}, Salary: {self.salary}"

    def update_salary(self, new_salary):
        self.salary = new_salary

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def total_salary_expenditure(self):
        return sum(employee.salary for employee in self.employees)

    def display_employees(self):
        for employee in self.employees:
            print(employee.display_details())


department = Department("IT Department")
employee1 = Employee("Alice", "E123", 50000)
employee2 = Employee("Bob", "E124", 60000)

department.add_employee(employee1)
department.add_employee(employee2)

print(f"Total Salary Expenditure: {department.total_salary_expenditure()}")
department.display_employees()

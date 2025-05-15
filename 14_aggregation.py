class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name, employees=None):
        self.name = name
        self.employees = employees or []
    
    def add_employee(self, employee):
        self.employees.append(employee)

# Test
emp1 = Employee("Alice")
dept = Department("IT")
dept.add_employee(emp1)
print(dept.employees[0].name)
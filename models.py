class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Payroll:
    def __init__(self, employee):
        self.employee = employee

    def calculate_net_salary(self):
        # Placeholder for net salary calculation logic
        return self.employee.salary

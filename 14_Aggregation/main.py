class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee

class Employee:
    def __init__(self, name):
        self.name = name

emp = Employee("John")
dep = Department("HR", emp)
print(dep.employee.name)
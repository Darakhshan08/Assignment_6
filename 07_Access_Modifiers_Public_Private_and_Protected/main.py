class Employee:
    def __init__(self):
        self.name = "Ali"
        self._salary = 50000
        self.__ssn = "123-45-6789"

emp = Employee()
print(emp.name)           # Public
print(emp._salary)        # Protected (can access but not recommended)
# print(emp.__ssn)        # Private (will cause AttributeError)
print(emp._Employee__ssn) # Accessing private using name mangling

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public
        self._salary = salary     # Protected
        self.__ssn = ssn          # Private

# Test
e = Employee("John", 50000, "123-45-6789")
print(e.name)
print(e._salary)
# print(e.__ssn)  # This would cause an error
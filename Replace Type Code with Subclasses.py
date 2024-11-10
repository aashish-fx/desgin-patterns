from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self._name = name

    @staticmethod
    def create_employee(name, employee_type):
        if employee_type == "Engineer":
            return Engineer(name)
        elif employee_type == "Manager":
            return Manager(name)
        elif employee_type == "Salesman":
            return Salesman(name)
        else:
            raise ValueError("Invalid employee type")

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def get_employee_type(self):
        pass

class Engineer(Employee):
    def __init__(self, name):
        super().__init__(name)

    def calculate_salary(self):
        return 50000  # Placeholder value

    def get_employee_type(self):
        return "Engineer"

class Manager(Employee):
    def __init__(self, name):
        super().__init__(name)

    def calculate_salary(self):
        return 70000  # Placeholder value

    def get_employee_type(self):
        return "Manager"

class Salesman(Employee):
    def __init__(self, name):
        super().__init__(name)

    def calculate_salary(self):
        return 60000  # Placeholder value

    def get_employee_type(self):
        return "Salesman"

# Usage:
employee1 = Employee.create_employee("Alice", "Engineer")
employee2 = Employee.create_employee("Bob", "Manager")
employee3 = Employee.create_employee("Charlie", "Salesman")

print(employee1.get_employee_type(), ":", employee1.calculate_salary())
print(employee2.get_employee_type(), ":", employee2.calculate_salary())
print(employee3.get_employee_type(), ":", employee3.calculate_salary())



# Use Self Encapsulate Field to create a getter for the field that contains type code.

# Make the superclass constructor private. Create a static factory method with the same parameters as the superclass constructor. It must contain the parameter that will take the starting values of the coded type. Depending on this parameter, the factory method will create objects of various subclasses. To do so, in its code you must create a large conditional but, at least, it will be the only one when it is truly necessary; otherwise, subclasses and polymorphism will do.

# Create a unique subclass for each value of the coded type. In it, redefine the getter of the coded type so that it returns the corresponding value of the coded type.

# Delete the field with type code from the superclass. Make its getter abstract.

# Now that you have subclasses, you can start to move the fields and methods from the superclass to corresponding subclasses (with the help of Push Down Field and Push Down Method).

# When everything possible has been moved, use Replace Conditional with Polymorphism in order to get rid of conditions that use the type code once and for all.


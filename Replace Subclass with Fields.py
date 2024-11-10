# Problem
# You have subclasses differing only in their (constant-returning) methods.

# Solution
# Replace the methods with fields in the parent class and delete the subclasses.

class Shape:
    def __init__(self, name, constant_area):
        self.name = name
        self._constant_area = constant_area

    @classmethod
    def create_shape(cls, name, constant_area):
        return cls(name, constant_area)

    def area(self):
        return self._constant_area

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name, 3.14 * radius ** 2)
        self.radius = radius

    @classmethod
    def create_shape(cls, name, radius):
        return super().create_shape(name, 3.14 * radius ** 2)

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name, width * height)
        self.width = width
        self.height = height

    @classmethod
    def create_shape(cls, name, width, height):
        return super().create_shape(name, width * height)

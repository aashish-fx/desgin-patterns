class ProductType:
    def __init__(self, type_code):
        self._type_code = type_code

    @property
    def type_code(self):
        return self._type_code

    @staticmethod
    def create_type_A():
        return ProductType("A")

    @staticmethod
    def create_type_B():
        return ProductType("B")

class Product:
    def __init__(self, name, product_type):
        self._name = name
        self._product_type = product_type

    @property
    def name(self):
        return self._name

    @property
    def product_type(self):
        return self._product_type.type_code

    @product_type.setter
    def product_type(self, type_code):
        if type_code == "A":
            self._product_type = ProductType.create_type_A()
        elif type_code == "B":
            self._product_type = ProductType.create_type_B()
        else:
            raise ValueError("Invalid product type")

# Example usage:
product_a = Product("Product A", ProductType.create_type_A())
print(product_a.name)             # Output: Product A
print(product_a.product_type)     # Output: A

product_a.product_type = "B"
print(product_a.product_type)     # Output: B


#Create a new class and give it a new name that corresponds to the purpose of the coded type. Here we will call it type class.
# Copy the field containing type code to the type class and make it private. Then create a getter for the field. A value will be set for this field only from the constructor.

# For each value of the coded type, create a static method in type class. It will be creating a new type class object corresponding to this value of the coded type.

# In the original class, replace the type of the coded field with type class. Create a new object of this type in the constructor as well as in the field setter. Change the field getter so that it calls the type class getter.

# Replace any mentions of values of the coded type with calls of the relevant type class static methods.

# Remove the coded type constants from the original class.
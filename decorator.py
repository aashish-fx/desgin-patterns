# Aggregation/composition is the key principle behind many design patterns, including Decorator. 
# "Wrapper” is the alternative nickname for the Decorator pattern that clearly expresses the main idea of the pattern. A wrapper is an object that can be linked with some target object.
# Use the Decorator pattern when you need to be able to assign extra behaviors to objects at runtime without breaking the code that uses these objects.
# Use the pattern when it’s awkward or not possible to extend an object’s behavior using inheritance.
# Decorator is a structural pattern that allows adding new behaviors to objects dynamically by placing them inside special wrapper objects, called decorators.

# // The component interface defines operations that can be
# // altered by decorators.
# interface DataSource is
#     method writeData(data)
#     method readData():data

# // Concrete components provide default implementations for the
# // operations. There might be several variations of these
# // classes in a program.
# class FileDataSource implements DataSource is
#     constructor FileDataSource(filename) { ... }

#     method writeData(data) is
#         // Write data to file.

#     method readData():data is
#         // Read data from file.

# // The base decorator class follows the same interface as the
# // other components. The primary purpose of this class is to
# // define the wrapping interface for all concrete decorators.
# // The default implementation of the wrapping code might include
# // a field for storing a wrapped component and the means to
# // initialize it.
# class DataSourceDecorator implements DataSource is
#     protected field wrappee: DataSource

#     constructor DataSourceDecorator(source: DataSource) is
#         wrappee = source

#     // The base decorator simply delegates all work to the
#     // wrapped component. Extra behaviors can be added in
#     // concrete decorators.
#     method writeData(data) is
#         wrappee.writeData(data)

#     // Concrete decorators may call the parent implementation of
#     // the operation instead of calling the wrapped object
#     // directly. This approach simplifies extension of decorator
#     // classes.
#     method readData():data is
#         return wrappee.readData()

# // Concrete decorators must call methods on the wrapped object,
# // but may add something of their own to the result. Decorators
# // can execute the added behavior either before or after the
# // call to a wrapped object.
# class EncryptionDecorator extends DataSourceDecorator is
#     method writeData(data) is
#         // 1. Encrypt passed data.
#         // 2. Pass encrypted data to the wrappee's writeData
#         // method.

#     method readData():data is
#         // 1. Get data from the wrappee's readData method.
#         // 2. Try to decrypt it if it's encrypted.
#         // 3. Return the result.

# // You can wrap objects in several layers of decorators.
# class CompressionDecorator extends DataSourceDecorator is
#     method writeData(data) is
#         // 1. Compress passed data.
#         // 2. Pass compressed data to the wrappee's writeData
#         // method.

#     method readData():data is
#         // 1. Get data from the wrappee's readData method.
#         // 2. Try to decompress it if it's compressed.
#         // 3. Return the result.


# // Option 1. A simple example of a decorator assembly.
# class Application is
#     method dumbUsageExample() is
#         source = new FileDataSource("somefile.dat")
#         source.writeData(salaryRecords)
#         // The target file has been written with plain data.

#         source = new CompressionDecorator(source)
#         source.writeData(salaryRecords)
#         // The target file has been written with compressed
#         // data.

#         source = new EncryptionDecorator(source)
#         // The source variable now contains this:
#         // Encryption > Compression > FileDataSource
#         source.writeData(salaryRecords)
#         // The file has been written with compressed and
#         // encrypted data.


# // Option 2. Client code that uses an external data source.
# // SalaryManager objects neither know nor care about data
# // storage specifics. They work with a pre-configured data
# // source received from the app configurator.
# class SalaryManager is
#     field source: DataSource

#     constructor SalaryManager(source: DataSource) { ... }

#     method load() is
#         return source.readData()

#     method save() is
#         source.writeData(salaryRecords)
#     // ...Other useful methods...


# // The app can assemble different stacks of decorators at
# // runtime, depending on the configuration or environment.
# class ApplicationConfigurator is
#     method configurationExample() is
#         source = new FileDataSource("salary.dat")
#         if (enabledEncryption)
#             source = new EncryptionDecorator(source)
#         if (enabledCompression)
#             source = new CompressionDecorator(source)

#         logger = new SalaryManager(source)
#         salary = logger.load()
#     // ...



class Component():
    """
    The base Component interface defines operations that can be altered by
    decorators.
    """

    def operation(self) -> str:
        pass


class ConcreteComponent(Component):
    """
    Concrete Components provide default implementations of the operations. There
    might be several variations of these classes.
    """

    def operation(self) -> str:
        return "ConcreteComponent"


class Decorator(Component):
    """
    The base Decorator class follows the same interface as the other components.
    The primary purpose of this class is to define the wrapping interface for
    all concrete decorators. The default implementation of the wrapping code
    might include a field for storing a wrapped component and the means to
    initialize it.
    """

    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        """
        The Decorator delegates all work to the wrapped component.
        """

        return self._component

    def operation(self) -> str:
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    """
    Concrete Decorators call the wrapped object and alter its result in some
    way.
    """

    def operation(self) -> str:
        """
        Decorators may call parent implementation of the operation, instead of
        calling the wrapped object directly. This approach simplifies extension
        of decorator classes.
        """
        return f"ConcreteDecoratorA({self.component.operation()})"


class ConcreteDecoratorB(Decorator):
    """
    Decorators can execute their behavior either before or after the call to a
    wrapped object.
    """

    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"


def client_code(component: Component) -> None:
    """
    The client code works with all objects using the Component interface. This
    way it can stay independent of the concrete classes of components it works
    with.
    """

    # ...

    print(f"RESULT: {component.operation()}", end="")

    # ...


if __name__ == "__main__":
    # This way the client code can support both simple components...
    simple = ConcreteComponent()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")

    # ...as well as decorated ones.
    #
    # Note how decorators can wrap not only simple components but the other
    # decorators as well.
    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Client: Now I've got a decorated component:")
    client_code(decorator2)

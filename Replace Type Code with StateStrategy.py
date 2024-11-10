# Problem
# You have a coded type that affects behavior but you cannot use subclasses to get rid of it.

# Solution
# Replace type code with a state object. If it is necessary to replace a field value with type code, another state object is “plugged in”.

from abc import ABC, abstractmethod

# Step 2: Create a new class for representing states/strategies
class State(ABC):
    @abstractmethod
    def get_type_code_value(self):
        pass

    @staticmethod
    def create_state(type_code):
        if type_code == 'A':
            return StateA()
        elif type_code == 'B':
            return StateB()
        else:
            raise ValueError("Invalid type code")

# Step 3: Create subclasses for each value of the type code
class StateA(State):
    def get_type_code_value(self):
        return "State A"

class StateB(State):
    def get_type_code_value(self):
        return "State B"

# Step 5: Original class with coded field changed to State class
class MyClass:
    def __init__(self, type_code):
        self._state = State.create_state(type_code)

    # Step 1: Use Self Encapsulate Field
    def get_type_code(self):
        return self._state.get_type_code_value()

    # Setter calls factory state method
    def set_type_code(self, type_code):
        self._state = State.create_state(type_code)

# Example usage:
obj = MyClass('A')
print(obj.get_type_code())  # Output: State A

obj.set_type_code('B')
print(obj.get_type_code())  # Output: State B

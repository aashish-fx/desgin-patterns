class CollectionManager:
    def __init__(self):
        self._collection = []  # Assign an empty list as the initial value

    # Getter for the collection (read-only)
    @property
    def collection(self):
        return tuple(self._collection)  # Return a read-only representation

    # Method for adding elements to the collection
    def add_element(self, element):
        self._collection.append(element)

    # Method for deleting elements from the collection
    def delete_element(self, element):
        if element in self._collection:
            self._collection.remove(element)
        else:
            print("Element not found in the collection.")

    # Setter (renamed to replace) for the collection
    def replace_collection(self, new_collection):
        self._collection = list(new_collection)

# Client code
manager = CollectionManager()

# Adding elements
manager.add_element(1)
manager.add_element(2)
manager.add_element(3)
print(manager.collection)  # Output: (1, 2, 3)

# Deleting an element
manager.delete_element(2)
print(manager.collection)  # Output: (1, 3)

# Replacing the collection
manager.replace_collection([4, 5, 6])
print(manager.collection)  # Output: (4, 5, 6)

# Methods for adding and deleting collection elements (add_element and delete_element) are created. They accept collection elements as parameters.
# An empty list is assigned to the _collection field in the class constructor (__init__) if not done so already.
# The setter for the collection field is renamed to replace_collection, as it's used to replace all collection elements with other ones.
# Client code that changes the collection directly should be replaced with calls to the add_element and delete_element methods.
# The getter for the collection is modified to return a read-only representation using the @property decorator and converting the list to a tuple.
# Finally, inspect client code to identify operations that modify the collection. If these operations logically belong to the collection class itself, they can be moved into the class as methods.
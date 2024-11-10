# Problem
# You have a conditional that performs various actions depending on object type or properties.

# Solution
# Create subclasses matching the branches of the conditional. 
# In them, create a shared method and move code from the corresponding branch of the conditional to it. 
# Then replace the conditional with the relevant method call. The result is that the proper implementation will be attained via polymorphism depending on the object class.
class Bird:
    # ...
    def getSpeed(self):
        pass

class European(Bird):
    def getSpeed(self):
        return self.getBaseSpeed()
    
    
class African(Bird):
    def getSpeed(self):
        return self.getBaseSpeed() - self.getLoadFactor() * self.numberOfCoconuts


class NorwegianBlue(Bird):
    def getSpeed(self):
        return 0 if self.isNailed else self.getBaseSpeed(self.voltage)

# Somewhere in client code
speed = Bird.getSpeed()

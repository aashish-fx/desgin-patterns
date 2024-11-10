from abc import ABC, abstractmethod
from __future__ import annotations

# behavioral patterns

# strategy
# iterator
# observer
# command
# state


class Context:
    _state = None
    
    def __init__(self, state: State) -> None:
        self.transition_to(state)
    
    def transition_to(self, state: State):
        self._state = state
        self._state._context = self
    
    def request1(self):
        self._state.handle1()
    
    def request2(self):
        self._state.handle2()
        
    
class State(ABC):
    
    @property
    def context(self):
        self._context
    
    @context.setter
    def context(self, context):
        self._context = context
        
    @abstractmethod
    def handle1(self):
        pass
    
    @abstractmethod
    def handle2(self):
        pass
    
class ConcreteState1(State):
    
    def handle1(self):
        self.context.transition_to(ConcreteState2())
    
class ConcreteState2(State):
    def handle2(self):
        self.context.transition_to(ConcreteState1())
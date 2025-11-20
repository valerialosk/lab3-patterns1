from abc import ABC, abstractmethod

class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self):
        pass

class ConcreteImplementationA(Implementation):
    def operation_implementation(self):
        return "ConcreteImplementationA: Here's the result on platform A."

class ConcreteImplementationB(Implementation):
    def operation_implementation(self):
        return "ConcreteImplementationB: Here's the result on platform B."

class Abstraction:
    def __init__(self, implementation):
        self._implementation = implementation
    
    def operation(self):
        return f"Abstraction: Base operation with:\n{self._implementation.operation_implementation()}"
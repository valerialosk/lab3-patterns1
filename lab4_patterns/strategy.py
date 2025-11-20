from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid {amount} using Credit Card"

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid {amount} using PayPal"

class ShoppingCart:
    def __init__(self):
        self._payment_strategy = None
    
    def set_payment_strategy(self, strategy):
        self._payment_strategy = strategy
    
    def checkout(self, amount):
        if self._payment_strategy:
            return self._payment_strategy.pay(amount)
        return "Please set payment strategy first"
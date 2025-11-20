from strategy import ShoppingCart, CreditCardPayment, PayPalPayment
from chain_of_responsibility import ConcreteHandlerA, ConcreteHandlerB
from iterator import BookCollection
from proxy import RealSubject, Proxy
from bridge import Abstraction, ConcreteImplementationA, ConcreteImplementationB
from adapter import OldSystem, Adapter

def demo_strategy():
    print("=== Strategy Pattern ===")
    cart = ShoppingCart()
    
    cart.set_payment_strategy(CreditCardPayment())
    print(cart.checkout(100))
    
    cart.set_payment_strategy(PayPalPayment())
    print(cart.checkout(200))
    print()

def demo_chain_of_responsibility():
    print("=== Chain of Responsibility ===")
    handler_a = ConcreteHandlerA()
    handler_b = ConcreteHandlerB()
    
    handler_a.set_next(handler_b)
    
    print(handler_a.handle("A"))
    print(handler_a.handle("B"))
    print(handler_a.handle("C"))
    print()

def demo_iterator():
    print("=== Iterator Pattern ===")
    collection = BookCollection()
    collection.add_book("Book 1")
    collection.add_book("Book 2")
    collection.add_book("Book 3")
    
    for book in collection:
        print(book)
    print()

def demo_proxy():
    print("=== Proxy Pattern ===")
    real_subject = RealSubject()
    proxy = Proxy(real_subject)
    
    print(proxy.request())
    print()

def demo_bridge():
    print("=== Bridge Pattern ===")
    implementation_a = ConcreteImplementationA()
    abstraction = Abstraction(implementation_a)
    print(abstraction.operation())
    
    implementation_b = ConcreteImplementationB()
    abstraction = Abstraction(implementation_b)
    print(abstraction.operation())
    print()

def demo_adapter():
    print("=== Adapter Pattern ===")
    old_system = OldSystem()
    adapter = Adapter(old_system)
    
    print(f"Old system: {old_system.specific_request()}")
    print(f"Adapter: {adapter.request()}")
    print()

if __name__ == "__main__":
    demo_strategy()
    demo_chain_of_responsibility()
    demo_iterator()
    demo_proxy()
    demo_bridge()
    demo_adapter()
    print("🎉 All behavioral and structural patterns demonstrated!")
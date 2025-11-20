from singleton import ConfigurationManager
from factory_method import WordDocument, PDFDocument
from abstract_factory import WindowsButton, MacButton
from builder import ComputerBuilder

def main():
    print("=== Design Patterns Demo ===")
    
    # 1. Singleton
    print("\n1. Singleton Pattern:")
    config1 = ConfigurationManager()
    config2 = ConfigurationManager()
    print(f"Same instance? {config1 is config2}")
    
    # 2. Factory Method
    print("\n2. Factory Method Pattern:")
    word_doc = WordDocument()
    pdf_doc = PDFDocument()
    print(word_doc.open())
    print(pdf_doc.open())
    
    # 3. Abstract Factory
    print("\n3. Abstract Factory Pattern:")
    win_button = WindowsButton()
    mac_button = MacButton()
    print(win_button.render())
    print(mac_button.render())
    
    # 4. Builder
    print("\n4. Builder Pattern:")
    computer = ComputerBuilder().set_cpu("Intel i7").set_ram("16GB").set_storage("1TB").build()
    print(computer)

if __name__ == "__main__":
    main()
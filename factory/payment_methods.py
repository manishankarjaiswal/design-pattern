# payment_methods.py

from abc import ABC, abstractmethod

# Product (Interface)
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# Concrete Products (Payment Methods)
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paying {amount} using Credit Card.")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paying {amount} using PayPal.")

class BitcoinPayment(Payment):
    def pay(self, amount):
        print(f"Paying {amount} using Bitcoin.")

class GooglePayment(Payment):
    def pay(self, amount):
        print(f"Paying {amount} using Google.")
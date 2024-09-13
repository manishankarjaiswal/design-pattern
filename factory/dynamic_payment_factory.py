# dynamic_payment_factory.py

from inspect import getmembers, isclass, isabstract
import payment_methods

# Creator
class DynamicPaymentFactory:
    payment_dictionary = {}

    def __init__(self):
        self.load_payment_methods()

    def load_payment_methods(self):
        # Get all non-abstract classes from the payment_methods module
        members = getmembers(payment_methods, lambda m: isclass(m) and not isabstract(m))
        for name, _type in members:
            if isclass(_type) and issubclass(_type, payment_methods.Payment):
                self.payment_dictionary[name] = _type

    def create(self, payment_type: str):
        # Check if the requested payment method is available
        if payment_type in self.payment_dictionary:
            return self.payment_dictionary[payment_type]()
        else:
            raise ValueError(f"{payment_type} is not currently supported as a payment method.")

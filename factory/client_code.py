# client_code.py

from dynamic_payment_factory import DynamicPaymentFactory

# Initialize the dynamic factory
factory = DynamicPaymentFactory()

# Choose a payment method dynamically
payment_method = factory.create('PayPalPayment')
payment_method.pay(100)  # Outputs: "Paying 100 using PayPal."

payment_method = factory.create('BitcoinPayment')
payment_method.pay(200)  # Outputs: "Paying 200 using Bitcoin."

payment_method = factory.create('CreditCardPayment')
payment_method.pay(300)  # Outputs: "Paying 300 using Credit Card."

payment_method = factory.create('GooglePayment')
payment_method.pay(400)  # Outputs: "Paying 300 using Credit Card."

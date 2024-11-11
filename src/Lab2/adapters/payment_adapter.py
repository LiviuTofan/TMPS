from Lab2.domain.payment_interface import PaymentProcessor
from Lab2.domain.extern_payment_service import ExternalPaymentService

class PaymentAdapter(PaymentProcessor):
    def __init__(self, external_service, conversion_rate=1.0):
        self.external_service = external_service
        self.conversion_rate = conversion_rate  # Default rate is 1.0 (no conversion)

    def convert_to_dollars(self, amount_in_euros):
        if amount_in_euros <= 0:
            raise ValueError("Amount must be greater than zero.")
        return amount_in_euros * self.conversion_rate


    def process_payment(self, amount, currency="USD"):
        if currency == "EUR":
            amount_in_dollars = self.convert_to_dollars(amount)
            print(f"Converting {amount:.2f} EUR to {amount_in_dollars:.2f} USD.")
            print(f"\nThe total price in euros is: €{amount:.2f}")
        else:
            amount_in_dollars = amount

        self.external_service.make_payment(amount_in_dollars)

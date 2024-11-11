from domain.payment_interface import PaymentProcessor
from domain.extern_payment_service import ExternalPaymentService

class PaymentAdapter(PaymentProcessor):
    def __init__(self, external_service):
        self.external_service = external_service

    def process_payment(self, amount):
        self.external_service.make_payment(amount)

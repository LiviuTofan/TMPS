from Lab3.commands.command import Command

class PaymentCommand(Command):
    def __init__(self, payment_adapter, amount, currency):
        self.payment_adapter = payment_adapter
        self.amount = amount
        self.currency = currency

    def execute(self):
        self.payment_adapter.process_payment(self.amount, self.currency)

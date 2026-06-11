class Payment:
    def __init__(self,amount):
        self.amount = amount

    def pay(self):
        print(f"Processing payment of ₹{self.amount}")

class CashPayment(Payment):
    def __init__(self, amount):
        super().__init__(amount)

    def pay(self):
        print(f"₹{self.amount} paid in cash. Thank you!")

class UPIPayment(Payment):
    def __init__(self, amount, upi_id):
        super().__init__(amount)
        self.upi_id = upi_id
    
    def pay(self):
        print(f"₹{self.amount} paid via UPI to {self.upi_id}. Thank you!")

class CardPayment(Payment):
    def __init__(self, amount, last4digits):
        super().__init__(amount)
        self.last4digits = last4digits
    
    def pay(self):
        print(f"₹{self.amount} paid via card ending in {self.last4digits}. Thank you!")

payments = [
    CashPayment(500),
    UPIPayment(1000, "anant@upi"),
    CardPayment(2500, 4242)
]

for payment in payments:
    payment.pay()
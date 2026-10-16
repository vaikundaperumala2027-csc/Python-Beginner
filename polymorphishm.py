class UPI:
    def pay(self, amount):
        print("Paid using UPI:", amount)
class CreditCard:
    def pay(self, amount):
        print("Paid using Credit Card:", amount)
class CashOnDelivery:
    def pay(self, amount):
        print("Pay on delivery:", amount)
payments = [UPI(), CreditCard(), CashOnDelivery()]
for method in payments:
    method.pay(100000)
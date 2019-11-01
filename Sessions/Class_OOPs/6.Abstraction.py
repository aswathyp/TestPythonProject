# In the example there is an abstract class Payment that has an abstract method payment(). 
# There are two child classes CreditCardPayment and MobileWalletPayment derived from Payment 
# that implement the abstract method payment() as per their functionality.

# As a user we are abstracted from that implementation when an object of CreditCardPayment is created 
# and payment() method is invoked using that object, payment method of CreditCardPayment class is invoked. 
# When an object of MobileWalletPayment is created and payment() method is invoked using that object, 
# payment method of MobileWalletPayment class is invoked.

from abc import ABC, abstractmethod
class Payment(ABC):
    def print_slip(self, amount):
        print('Purchase of amount- ', amount)
    @abstractmethod
    def payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def payment(self, amount):
        print('Credit card payment of- ', amount)

class MobileWalletPayment(Payment):
    def payment(self, amount):
        print('Mobile wallet payment of- ', amount)

obj = CreditCardPayment()
obj.payment(100)
obj.print_slip(100)
print(isinstance(obj, Payment))
obj = MobileWalletPayment()
obj.payment(200)
obj.print_slip(200)
print(isinstance(obj, Payment))
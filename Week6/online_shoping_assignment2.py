
from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def calculate_price(self):
        pass


class PhysicalProduct(Product):
    def __init__(self, name, price, shipping_cost):
        super().__init__(name, price)
        self.shipping_cost = shipping_cost

    def calculate_price(self):
        return self.price + self.shipping_cost


class DigitalProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price)

    def calculate_price(self):
        return self.price

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid Rs. {amount:.2f} using Card Payment.")

class CashPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid Rs. {amount:.2f} using Cash Payment.")

class Order:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        return sum(
            product.calculate_price()
            for product in self.products
        )

    def display_order(self):
        print("\n========== ORDER DETAILS ==========")

        for product in self.products:
            print(
                f"{product.name}: "
                f"Rs. {product.calculate_price():.2f}"
            )

        print("-----------------------------------")
        print(f"Total Amount: Rs. {self.calculate_total():.2f}")

class Checkout:
    def __init__(self, order, payment_method):
        self.order = order
        self.payment_method = payment_method

    def process_payment(self):
        amount = self.order.calculate_total()

        print("\n========== CHECKOUT ===============")
        print(f"Amount to Pay: Rs. {amount:.2f}")

        self.payment_method.pay(amount)
        print("Checkout completed successfully!")

if __name__ == "__main__":

    keyboard = PhysicalProduct("Keyboard", 2500, 200)
    book = PhysicalProduct("Python Book", 1200, 150)
    ebook = DigitalProduct("Python E-book", 800)

    order = Order()
    order.add_product(keyboard)
    order.add_product(book)
    order.add_product(ebook)

    order.display_order()

    print("\n--- First Checkout: Card Payment ---")
    card_checkout = Checkout(order, CardPayment())
    card_checkout.process_payment()

    print("\n--- Second Checkout: Cash Payment ---")
    cash_checkout = Checkout(order, CashPayment())
    cash_checkout.process_payment()

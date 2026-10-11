class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, price):
        self.items.append({"product": product, "price": price})
        print(f"{product} added to the cart.")

    def calculate_total(self):
        return sum(item["price"] for item in self.items)

    def remove_item(self, product):
        for item in self.items:
            if item["product"].lower() == product.lower():
                self.items.remove(item)
                print(f"{product} removed from the cart.")
                return

        print(f"{product} not found in the cart.")

    def display_cart(self):
        print("\nShopping Cart:")

        if not self.items:
            print("Cart is empty.")
        else:
            for item in self.items:
                print(f"{item['product']}: Rs. {item['price']:.2f}")

        print(f"Total: Rs. {self.calculate_total():.2f}")


# Create two independent shopping carts
cart1 = ShoppingCart()
cart2 = ShoppingCart()


def manage_cart(cart, cart_name):
    while True:
        print(f"\n--- {cart_name} Menu ---")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Display Cart")
        print("4. Calculate Total")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            product = input("Enter product name: ")

            try:
                price = float(input("Enter product price (Rs.): "))

                if price < 0:
                    print("Price cannot be negative.")
                    continue

                cart.add_item(product, price)

            except ValueError:
                print("Please enter a valid price.")

        elif choice == "2":
            product = input("Enter product name to remove: ")
            cart.remove_item(product)

        elif choice == "3":
            cart.display_cart()

        elif choice == "4":
            print(f"Total: Rs. {cart.calculate_total():.2f}")

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")


# Save both shopping carts to result.txt
def save_results(cart1, cart2):
    with open("result.txt", "w") as file:
        for cart_name, cart in [("Cart 1", cart1), ("Cart 2", cart2)]:
            file.write(f"\n--- {cart_name} ---\n")

            if not cart.items:
                file.write("Cart is empty.\n")
            else:
                for item in cart.items:
                    file.write(
                        f"{item['product']}: Rs. {item['price']:.2f}\n"
                    )

            file.write(
                f"Total: Rs. {cart.calculate_total():.2f}\n"
            )

    print("All shopping cart data saved to result.txt.")


# Main program
while True:
    print("\n===== SHOPPING CART SYSTEM =====")
    print("1. Manage Cart 1")
    print("2. Manage Cart 2")
    print("3. Display Both Carts")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        manage_cart(cart1, "Cart 1")

    elif choice == "2":
        manage_cart(cart2, "Cart 2")

    elif choice == "3":
        print("\n--- Cart 1 ---")
        cart1.display_cart()

        print("\n--- Cart 2 ---")
        cart2.display_cart()

    elif choice == "4":
        print("Thank you for using the Shopping Cart System!")
        save_results(cart1, cart2)
        break

    else:
        print("Invalid choice. Please try again.")

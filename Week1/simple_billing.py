product_name = input("Enter Product Name: ")
price = float(input("Enter Price: "))
quantity = int(input("Enter Quantity: "))

def calculate_price(product_price, product_quantity):
    sub_total = product_price * product_quantity
    prod_discount = (10 * sub_total) / 100
    prod_total = sub_total - prod_discount
    return prod_total, prod_discount


final_amount, discount = calculate_price(price, quantity)


print(f"Total Amount = {final_amount}")

item_quantity = int(input("Enter the quantity of an item: "))
if item_quantity >= 1000:
    price_unit = 3
elif item_quantity <= 1000:
    price_unit = 5
extended_price = item_quantity * price_unit
tax = extended_price * 0.07
total = extended_price + tax
print(f"Extended price is ${extended_price}")
print(f"Tax is ${tax}")
print(f"Total is ${total}")
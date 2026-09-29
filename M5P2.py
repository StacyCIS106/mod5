item = str(input("Enter an item: "))
if item == "A":
    unit_price = 10
else:
    unit_price = 20
quantity = int(input("Enter the quantity: "))
extended_price = unit_price * quantity
print( item, quantity, unit_price, extended_price )
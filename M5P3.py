num_books = int(input("Enter the number of books: "))
cost_books = int(input("Enter the cost per book: "))
order_total = num_books * cost_books
if order_total > 50:
    shipping = 0
    print("$" + str(order_total), " shipping:$" + str(shipping))
else:
    shipping = 25
    print("$" + str(order_total), " shipping:$" + str(shipping))
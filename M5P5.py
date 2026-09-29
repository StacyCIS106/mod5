user_name = input("Enter your last name: ")
num_dep = int(input("Enter the number of dependents: "))
gros_income = int(input("Enter your gross income: "))
adj_gross_income = gros_income - (num_dep * 12000)
if adj_gross_income > 50000:
    tax_rate = 0.20
else:
    tax_rate = 0.10
income_tax = adj_gross_income * tax_rate
if income_tax < 0:
    income_tax = 100
print(user_name, gros_income, num_dep, adj_gross_income, income_tax)
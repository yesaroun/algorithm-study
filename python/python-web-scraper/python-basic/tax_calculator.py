
# Write your code here:
def get_yearly_revenue(month_revenue = 0):
    return month_revenue * 12

def get_yearly_expenses(month_expense = 0):
    return month_expense * 12

def get_tax_amount(profit = 0):
    result = 0
    if profit >= 100000:
        result = profit * 0.25
    else:
        result = profit * 0.15
    return result

def apply_tax_credits(tax_amount = 0, tax_credits = 1):
    return tax_amount - (tax_amount * tax_credits)

# Don't touch anthing below this line 🙅🏻‍♂️🙅🏻‍♀️

monthly_revenue = 5500000
monthly_expenses = 2700000
tax_credits = 0.01

profit = get_yearly_revenue(monthly_revenue) - get_yearly_expenses(monthly_expenses)

tax_amount = get_tax_amount(profit)

final_tax_amount = tax_amount - apply_tax_credits(tax_amount, tax_credits)

print(f"Your tax bill is: ${final_tax_amount}")


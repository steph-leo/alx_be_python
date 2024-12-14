# Prompt the user for their monthly income and total monthly expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with interest
annual_savings = monthly_savings * 12
projected_annual_savings = annual_savings + (annual_savings * 0.05)

# Display the results
print(f"Your monthly savings: ${monthly_savings:.2f}")
print(f"Projected annual savings after interest: ${projected_annual_savings:.2f}")

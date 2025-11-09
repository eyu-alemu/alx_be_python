# This program calculates monthly and projected annual savings based on user input.

# Ask the user for their monthly income
income = float(input("Enter your monthly income: "))

# Ask the user for their total monthly expenses
expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses

# Calculate projected annual savings with 5% interest
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

# Display the results
print("Your monthly savings are $", monthly_savings)
print("Projected savings after one year, with interest, is: $", projected_savings)

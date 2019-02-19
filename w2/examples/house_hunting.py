# Test case:
# Enter your annual salary: 120000
# Enter the percent of your salary to save, as a decimal: .10
# Enter the cost of your dream home: 1000000
# Number of months: 183

# Get my annual income
annual_salary = float(input("Enter your annual salary: "))

# Get how much I want to save each month
portion_saved = float(
    input("Enter the percent of your salary to save, as a decimal: "))

# Figure out my monthly income
monthly_salary = annual_salary / 12

# Figure out how much I'm saving each month as a percentage of my income
amount_saved_each_month = portion_saved * monthly_salary

# Get the price of the house and the percentage for the down payment
portion_down_payment = 0.25
total_cost = float(input("Enter the cost of your dream home: "))

# Calculate my down payment
down_payment = total_cost * portion_down_payment

# Set initial information
current_savings = 0
current_month = 0
interest_rate = 0.04

# Each month while our savings < down payment
while current_savings < down_payment:
    # add 1 to current_month
    current_month += 1

    # calculate interest -- current savings * rate (0.04) / 12
    interest = current_savings * interest_rate / 12
    # add interest to current savings
    current_savings += interest  # same as current_savings = current_savings + interest
    # add the amount I'm saving to my current savings
    current_savings += amount_saved_each_month

# Report how many months that took
print("Number of months:", current_month)

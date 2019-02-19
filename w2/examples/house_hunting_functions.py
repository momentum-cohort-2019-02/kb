# Test case:
# Enter your annual salary: 120000
# Enter the percent of your salary to save, as a decimal: .10
# Enter the cost of your dream home: 1000000
# Number of months: 183


def input_float(prompt):
    """Gets input from a user and converts it to a float."""
    return float(input(prompt))


def increment_savings(current_savings, interest_rate, amount_to_add=0):
    """Add interest to savings and then add the optional new savings."""
    return current_savings + (current_savings * interest_rate) + amount_to_add


def calculate_months_to_save_for_down_payment():
    # Get my annual income
    annual_salary = input_float("Enter your annual salary: ")
    # Get how much I want to save each month
    percent_saved = input_float(
        "Enter the percent of your salary to save, as a decimal: ")

    # Figure out my monthly income
    monthly_salary = annual_salary / 12

    # Figure out how much I'm saving each month as a percentage of my income
    saved_each_month = monthly_salary * percent_saved

    # Get the price of the house and the percentage for the down payment
    total_cost = input_float("Enter the cost of your dream home: ")
    percentage_down_payment = 0.25

    # Calculate my down payment
    down_payment = total_cost * percentage_down_payment

    # Set initial information
    total_savings = 0
    current_month = 0
    interest_rate = 0.04
    # Each month while our savings < down payment
    while total_savings < down_payment:
        # add 1 to current_month
        current_month += 1

        # calculate interest -- current savings * rate (0.04) / 12
        # add interest to current savings
        # add the amount I'm saving to my current savings
        total_savings = increment_savings(total_savings, interest_rate / 12,
                                          saved_each_month)

    # Report how many months that took
    print("Number of months:", current_month)


calculate_months_to_save_for_down_payment()

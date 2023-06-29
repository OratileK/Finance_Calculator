import math

def calculate_investment():
    principal = get_valid_float_input("Enter the amount of money that you are depositing: ")
    rate = get_valid_float_input("Enter the interest rate (as a percentage): ") / 100
    time = get_valid_float_input("Enter the number of years you plan on investing: ")
    interest = get_valid_interest_input("Enter 'simple' or 'compound' interest: ")

    if interest == "simple":
        investment = principal * (1 + rate * time)
        print("Your total investment after", time, "years will be", round(investment, 2))
    elif interest == "compound":
        investment = principal * math.pow((1 + rate), time)
        print("Your total investment after", time, "years will be", round(investment, 2))
    else:
        print("Please enter 'simple' or 'compound' to proceed.")

def calculate_bond():
    house_value = get_valid_float_input("Enter the present value of the house: ")
    interest_rate = get_valid_float_input("Enter the interest rate (as a percentage): ") / 100
    months = get_valid_float_input("Enter the number of months over which the bond will be repaid: ")
    monthly_interest = interest_rate / 12

    repayment = (monthly_interest * house_value) / (1 - (1 + monthly_interest) ** (-months))
    print("The total repayment you will pay after", months, "months is", round(repayment, 2))

def get_valid_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_valid_interest_input(prompt):
    while True:
        value = input(prompt).lower()
        if value == "simple" or value == "compound":
            return value
        print("Invalid input. Please enter 'simple' or 'compound'.")

print("Investment - to calculate the amount of interest you will earn on your investment.")
print("Bond - to calculate the amount you will have to pay on a home loan.")

calc_option = input("Please enter an option from the above menu. Type in 'investment' or 'bond' to proceed: ").lower()

if calc_option == "investment":
    calculate_investment()
elif calc_option == "bond":
    calculate_bond()
else:
    print("Enter a valid input!")

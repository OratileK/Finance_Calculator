import math


def get_investment_input():
    principal = float(input("Enter the amount of money that you are depositing: "))
    rate = float(input("Enter the interest rate (as a percentage): ")) / 100
    time = float(input("Enter the number of years you plan on investing: "))
    interest = input("Enter 'simple' or 'compound' interest: ").lower()
    return principal, rate, time, interest


def calculate_investment(principal, rate, time, interest):
    if interest == "simple":
        investment = principal * (1 + rate * time)
    elif interest == "compound":
        investment = principal * math.pow((1 + rate), time)
    else:
        raise ValueError("Invalid interest type, use 'simple' or 'compound'.")
    return investment


def get_bond_input():
    house_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): ")) / 100
    months = float(input("Enter the number of months over which the bond will be repaid: "))
    return house_value, interest_rate, months


def calculate_bond(house_value, interest_rate, months):
    monthly_interest = interest_rate / 12
    repayment = (monthly_interest * house_value) / (1 - (1 + monthly_interest) ** (-months))
    return repayment


def main():
    print("Investment - to calculate the amount of interest you will earn on your investment.")
    print("Bond - to calculate the amount you will have to pay on a home loan.")
    calc_option = input(
        "Please enter an option from the above menu. Type in 'investment' or 'bond' to proceed: ").lower()

    if calc_option == "investment":
        principal, rate, time, interest = get_investment_input()
        try:
            investment = calculate_investment(principal, rate, time, interest)
            print(f"Your total investment after {time} years will be {investment:.2f}")
        except ValueError as e:
            print(e)

    elif calc_option == "bond":
        house_value, interest_rate, months = get_bond_input()
        repayment = calculate_bond(house_value, interest_rate, months)
        print(f"The total repayment you will pay after {months} months is {repayment:.2f}")

    else:
        print("Enter a valid input!")


if __name__ == "__main__":
    main()

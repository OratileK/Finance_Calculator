import math

print("Investment - to calculate the amount of interest you will earn on your investment.")
print("Bond - to calculate the amount you will have to pay on a home loan.")
# ask user to enter an option from the above menu
calc_option = input("Please enter an option from the above menu. Type in 'investment' or 'bond' to proceed: ").lower()
#calc_option = input().lower() # to ensure that the users input is in lowercase

# Check if the user entered a valid option
if calc_option == "investment":
        principal = float(input("Enter the amount of money that you are depositing: "))
        rate = float(input("Enter the interest rate (as a percentage): ")) / 100 # the number of the interest rate should be entered
        time = float(input("Enter the number of years you plan on investing: "))
        interest = input("Enter 'simple' or 'compound' interest: ").lower() # ensures that users input is in lower case
        
        # interest calculations
        if interest == "simple":
            investment = principal * (1 + rate * time)
            print("Your total investment after", time, "years will be", round(investment,2)) # print results to 2 decimal places
        elif interest == "compound":
            investment = principal * math.pow((1 + rate), time)
            print("Your total investment after", time, "years will be", round(investment,2))
        else:
            print("Please enter 'simple' or 'compound' to proceed.")
    
    # Bond calculations
elif calc_option == "bond":
        # Get user input
        house_value = float(input("Enter the present value of the house: "))
        interest_rate = float(input("Enter the interest rate (as a percentage): ")) / 100
        months = float(input("Enter the number of months over which the bond will be repaid: "))
        monthly_interest = interest_rate / 12
        # calculate repayment
        repayment = (monthly_interest * house_value) / (1 - (1 + monthly_interest) ** (-months))
        print("The total repayment you will pay after", months, "months is", round(repayment,2)) # amount user will repay each month based on their input
else:
        print("Enter a valid input!")

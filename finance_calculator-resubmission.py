import math
# finance_calculators.py
#________________________
# This is a program for calculating simple, and compound investments and
# bond repayments per month. 
#________________________

# Pseudocode start
# Declare variable for investment and bond then ask for input of investment
# Or bond. If investment get detaisl and ask simple or compound. 
# calcualte for simple and compound with details.
# If bond calculate ask for details of bond then calcualte for bond.

print("investment - to calculate the amount of interest you'll \
earn on your investment.")
print("bond - to calculate the amoun you'll have to pay \
on a home loan.")

investment = "investment"

bond = "bond"

investment_or_bond = input("enter either investment or bond \
from the menu above.")
investment_or_bond = investment_or_bond.lower()

if investment_or_bond == investment:
    print("investment")
elif investment_or_bond == bond:
    print("bond")
else:
    print("please re-enter investment or bond")

if investment_or_bond == investment:
    amnt_money = float(input("enter your deposit"))
    intrest_rate = float(input("enter interest rate"))
    calc_rate = intrest_rate / 100
    num_years = float(input("enter number of years to be invested"))
    simple_or_compound = input("enter simple or compound interest")

    if simple_or_compound == "simple":
        interest = "simple"
        mature_investment = amnt_money * (1 + calc_rate * num_years)
        rnd_mature_inv = round(mature_investment, 2)
        print(f"Mature investment is equal to {rnd_mature_inv}")
    elif simple_or_compound == "compound":
        interest = "compound"
        mature_investment = amnt_money * math.pow(( 1 + calc_rate),num_years)
        rnd_mature_inv = round(mature_investment, 2)
        print(f"Mature investment is equal to {rnd_mature_inv}")
    else:
        print("You didnt enter simple or compound, please restart program")

elif investment_or_bond == bond:
    current_val_house = float(input("enter current value house"))
    intrest_rate = float(input("enter interest rate"))
    calc_rate = intrest_rate / 100 / 12
    num_pay_months = int(input("enter number of months to pay bond"))
    repayment = (calc_rate * current_val_house)/(1 - (1 + calc_rate)** \
        ( - num_pay_months))
    rnd_repayment= round(repayment, 2)
    print(f"You will pay R{rnd_repayment} per month")

else:
    print("You didn't enter invesetment or bond, please restart program")
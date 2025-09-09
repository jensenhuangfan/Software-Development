customer_name = input("Welcome, what is your name? ")

starting_balance = float(5000.25)

print(f"Hello, {customer_name}, your starting balance is ${starting_balance}")
pay_check = float(input("How much would you like to deposit? $"))
expenditure_item= input("What did you buy? ")
expenditure = float(input("How much does " + expenditure_item + " cost? $"))
# def checking_balance (customer_name, starting_balance, pay_check, expenditure_item, expenditure): WAS WRONG
def checking_balance():
    ending_balance = starting_balance + pay_check - expenditure
    print(f"Good day {customer_name} After spending money on a {expenditure_item}, in the amount of, {expenditure}, your current checking balance is: $, {ending_balance}")
checking_balance()
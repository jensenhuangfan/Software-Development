#number of credits to graduate = 120. Write the statement below to check.
#Constant credits_to_gradutate
credits_to_gradutate = 120


def check_credits():
        numb_credits = numb_credits = int(input("How many credits do you have? "))

        if numb_credits >= credits_to_gradutate:
            print(f"Congrates u smart!")
            option_to_run_again()
        else:
              numb_short = credits_to_gradutate - numb_credits
              print(f"you dumb, u need {numb_short} to graduate.")
              option_to_run_again()
def option_to_run_again():        
        run_again = input("Do you want to run again? y/n ")
        if run_again == "y":
              check_credits()
        elif run_again == "n":
              print("bye")
        else:
              run_again = input("Do you want to run again? y/n ")
        if run_again == "y":
              check_credits()
        elif run_again == "n":
              print("bye")
        else:
              print("U too stupid to graduate if u cant read!")

check_credits()
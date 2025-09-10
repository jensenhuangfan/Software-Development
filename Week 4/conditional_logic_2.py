#number of credits to graduate = 120. Write the statement below to check.
#Constant credits_to_gradutate
credits_to_gradutate = 120


def check_credits():
        numb_credits = numb_credits = int(input("How many credits do you have? "))

        if numb_credits >= credits_to_gradutate:
            print(f"Congrates u smart!")
        else:
              numb_short = credits_to_gradutate - numb_credits
              print(f"you dumb, u need {numb_short} to graduate.")

check_credits()
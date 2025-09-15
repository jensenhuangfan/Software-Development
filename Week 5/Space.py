def weight_convertion():
    weight = float(input("Codey, how much do you weigh in LB? DONT USE LETTERS IT WILL FAIL! "))
    mercury_weight = weight / 100 * 90
    venus_weight  = weight / 100 * 91
    mars_weight = weight / 100 * 38
    jupiter_weight = weight / 100 * 234
    saturn_weight  = weight / 100 * 106
    uranus_weight  = weight / 100 * 92
    neptune_weight = weight / 100 * 119
    pluto_weight = weight / 100 * 6.3

    print(f"""
     Mercury Weight = {mercury_weight}LB
     Venus Weight = {venus_weight}LB
     Mars Weight = {mars_weight}LB
     Jupiter Weight = {jupiter_weight}LB
     Saturn Weight = {saturn_weight}LB
     Uranus Weight = {uranus_weight}LB
     Neptune Weight = {neptune_weight}LB
     Pluto Weight = {pluto_weight}LB""")
    option_to_run_again()


def option_to_run_again():        
        run_again = input("Do you want to run again? y/n or Y/N: ")
        if run_again == "y":
              weight_convertion()
        elif run_again == "Y":
            weight_convertion()
        elif run_again == "n":
              print("bye")
        elif run_again == "N":
              print("bye")
        else:
              run_again = input("Wrong Input, Do you want to run again? y/n or Y/N: ")
        if run_again == "y":
              weight_convertion()
        elif run_again == "Y":
            weight_convertion()
        elif run_again == "n":
              print("bye")
        elif run_again == "N":
              print("bye")
        else:
              print("U too stupid brawn for brains!")

weight_convertion()
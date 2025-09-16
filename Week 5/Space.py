autorun = True
while autorun:
      name = input("What's your name boxer? ")
      weight = float(input(f"{name}, how much do you weigh in LB? DONT USE LETTERS IT WILL FAIL! "))
      mercury_weight = weight / 100 * 90
      venus_weight  = weight / 100 * 91
      mars_weight = weight / 100 * 38
      jupiter_weight = weight / 100 * 234
      saturn_weight  = weight / 100 * 106
      uranus_weight  = weight / 100 * 92
      neptune_weight = weight / 100 * 119
      pluto_weight = weight / 100 * 6.3

      print(f"""{name} here are your weights in each of the planets in the solar system
      Mercury Weight = {mercury_weight}LB
      Venus Weight = {venus_weight}LB
      Mars Weight = {mars_weight}LB
      Jupiter Weight = {jupiter_weight}LB
      Saturn Weight = {saturn_weight}LB
      Uranus Weight = {uranus_weight}LB
      Neptune Weight = {neptune_weight}LB
      Pluto Weight = {pluto_weight}LB""")


#AI coached, taught me about while loops for python
      run_again = input("Do you want to run again? y/n ")
      if run_again != "y":
            autorun = False
            print(f"Have a good day {name}")
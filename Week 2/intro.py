# Below are my notes for coding.
# Here are more ptactice notes.

# Print Statement - This is used to output to the terminal AKA Console.

print("Mr. Sekol is the coolest teacher in the universe aske Mr. Wright.")

#Variables - These can change value based on user input or you can just assign a value to them

player_name = "Jeff"
#concatention - combine strings + variables to form an output
print("welcome "+player_name+" it's great to have you here.")
print(player_name)
player_name= "JFK" #changed the name of the variable
print("welcome ",player_name," it's great to have you here.") #you can use "," instead of "+" but the , makes more spacing

#pass therough the vaiable into the output
print(f"Welcome, {player_name}, it's great to have you here.") # with the f in front of the string we can pass through the value of the variable

#User Input - create a variable and ask user for input.

country_of_origin = input(f"Well {player_name}, can you tell me the country you're from ")

if country_of_origin == "Ukraine":
    print(f"{player_name}, LMAO bros in the trenches")
elif country_of_origin == "ukraine":
    print(f"{player_name}, LMAO bros in the trenches")

else: print(f"{player_name} is from {country_of_origin}")
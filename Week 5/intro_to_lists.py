# List [] <-- Square Brackets = list

#Fav restraunts

fav_rest = ["Sheetz", "Pizza Hut", "Inter Circle", "Bruster's", "Arby's", "Dominos", "DQ", "Coaches", "KFC", "Taco Bell", "Waffles Incaffeinated"]

print(fav_rest)
print(fav_rest[0])
print(fav_rest[1])
print(fav_rest[2])
print(fav_rest[3])
print(fav_rest[4])
print(fav_rest[5])
print(fav_rest[6])
print(fav_rest[7])
print(fav_rest[8])
print(fav_rest[9])
print(fav_rest[10])
fav_rest.append("BK")
print(fav_rest[11])
# print(fav_rest[12]) kills it since counting starts at 0 and were out of the list range


for item in fav_rest:
    print(f"I like to eat {item}.")
# Main Quest - Creating a Character Sheet
player_character = {
    "name":"Ninjafiveo",
    "class":"Mage",
    "Mana":100,
    "guild":"Arcus",
    "is_active":True,
    "inventory":["Staff of Coding", "Book of Python", "Mana Potion of Starbucks"],
    "health":90,
}

print(f"Character Name: {player_character['name']}")
print(f"Remaining Health: {player_character['health']}")
print(f"Current Inventory: {player_character['inventory']}")
print(f"{player_character['name']} first inventory item is {player_character['inventory'][0]}")

#modify Dictionary
player_character["name"] = "Ninja the Senior Dev"
print(f"Character Name: {player_character['name']}")
player_character["level"] = 100
print(f"Character Level: {player_character['level']}")


#Iterate over dictionary
print("\n=== Looping through Keys ---")
for stat_key in player_character:
    print(f"Stat Key: {stat_key} | Value : {player_character[stat_key]}")

print(f"\n--- Looping through values ---")
#use the .values() method
for stat_value in player_character.values():
    print(f"Value: {stat_value}")

print("\n--- Looping through key-value pairs (The Best Way?) ---")
for key, value in player_character.items():
    print(f"{key.title()}: {value}")

# inventory_test = ["Staff of Coding", "Book of Python", "Mana Potion of Starbucks"]
# print(inventory_test[2])
# inventory_test.insert(1, "Keyboard of Sloth")
# ['Staff of Coding', 'Keyboard of Sloth', 'Book of Python', 'Mana Potion of Starbucks']
# print(inventory_test[2]) 
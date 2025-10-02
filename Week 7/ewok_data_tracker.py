# Ewok Data Tracker - Created by JensenHuangFan

ewok_data = {
    "name": "Jeff",
    "age": 21,
    "weapon": "Gun",
    "rank": "Warrior"
}

print("Ewok Name:", ewok_data["name"])
print("Ewok Age:", ewok_data["age"])
print("Ewok Weapon:", ewok_data["weapon"])
print("Ewok Rank:", ewok_data["rank"])

ewok_data["weapon"] = "Nukes"  # Updating the weapon
ewok_data["rank"] = "MasterChief"  # Updating the rank
ewok_data["homeworld"] = "Earth"  # Adding a new attribute for homeworld
ewok_data["Nickname"] = "Oppenhimer"

print("\nUpdated Ewok Data:")
for key, value in ewok_data.items():
    print(f"{key}: {value}")

ewok_tribe = {
    "Wicket": ewok_data,
    "Chief Chirpa": {
        "name": "Chief Chirpa",
        "age": 30,
        "weapon": "Staff",
        "rank": "Chief",
        "homeworld": "Endor"
    }
}


print("\nEwok Tribe Data:")
for ewok_name, ewok_info in ewok_tribe.items():
    print(f"\nEwok: {ewok_name}")
    for key, value in ewok_info.items():
        print(f"{key}: {value}")
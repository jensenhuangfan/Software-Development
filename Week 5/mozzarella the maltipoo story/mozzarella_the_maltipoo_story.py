print("=== mozzarella the maltipoo adventure ===")
print("Type 'help' for commands. \n")

#game stats
current_location = "home" #starting place
locations = ["starbucks", "cinemark", "park", "school"]
exits = [
    ["starbucks", "cinemark", "park", "school"], #starbucks exits
    ["home", "cinemark", "park", "school"], #home exits
    ["starbucks", "home", "park", "school"], #cinemark exits
    ["starbucks", "cinemark", "home", "school"], #park exits
    ["starbucks", "cinemark", "park", "home"] #school exits
    ]               # parallel lists example (room -> exits list index)


inventory = []

money = int(0)
moz_points = int(0)
turns_left = 20
has_won = False
is_running = True

def show_help():
    print("Commands: look, go <location>, take <item>, use <item>, inv, help, quit")

def show_location():
    print(f"\nYou are at {current_location}.")
    # describe based on location
    if current_location == "school":
        print("You're working as a teacher so you can afford to take mozzarella the maltipoo on adventures.")
    elif current_location == "starbucks":
        print("your at starbucks working on your code while mozzarella the maltipoo is eatting tons of pup cups.")
    elif current_location == "cinemark":
        print("your watching the smerfs movie")
    elif current_location == "park":
        print("you take mozzarella the maltipoo on a walk.")
    else:
        print("You're wondering where to take mozzarella the maltipoo.")

def location_index(name):
    # map location name -> index in locations list (list practice; not using dict)
    for i, r in enumerate(locations):
        if r == name:
            return i
    return -1

def move_player(dest):
    global current_location
    cur_idx = location_index(current_location)
    if cur_idx == -1:
        print("You feel lost in the woods...")
        return
    if dest in exits[cur_idx]:
        current_location = dest
        locations()
    else:
        print("You can't go there from here.")

def use_item(item):
    global moz_points
    if current_location == "cinemark" and item == "ticket":
        print("You and mozzarella the maltipoo saw the smerfs movie")
        moz_points = moz_points + 5
    else:
        print("no usable items.")


def handle_command(cmd):
    parts = cmd.strip().lower().split()
    if not parts:
        return
    if parts[0] == "help":
        show_help()
    elif parts[0] == "look":
        show_location()
    elif parts[0] == "go" and len(parts) >= 2:
        move_player(parts[1])
    elif parts[0] == "take" and len(parts) >= 2:
        use_item(parts[1])
    elif parts[0] == "inv":
        print("Inventory:", inventory if inventory else "(empty)")
    elif parts[0] == "quit":
        global is_running
        is_running = False
    else:
        print("Unknown command. Type 'help'.")






# --- main loop ---
show_location()
while is_running and not has_won:
    # optional: pressure mechanic
    turns_left -= 1
    if turns_left <= 0:
        print("\nStormtroopers catch you in the forest. You lose.")
        break


    cmd = input("\n> ")
    handle_command(cmd)


if has_won:
    print("\nVictory! Thanks for playing.")
print("Game over.")
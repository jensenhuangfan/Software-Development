import random
print("=== mozzarella the maltipoo adventure ===")
print("Type 'help' for commands. \n")

#game stats
#game stats
current_location = "home" #starting place
locations = ["home", "starbucks", "cinemark", "park", "school", "road"]
exits = [
    ["starbucks", "cinemark", "park", "school"], # home exits
    ["home", "cinemark", "park", "school"], # starbucks exits
    ["starbucks", "home", "park", "school"], # cinemark exits
    ["starbucks", "cinemark", "home", "school"], # park exits
    ["starbucks", "cinemark", "park", "home"], # school exits
    ["starbucks", "cinemark", "park", "home", "school"] # road exits
]

inventory = []
buyable_items = ["Steak", "ticket",]

money = int(10)
moz_points = int(0)
turns_left = 20
has_won = False
is_running = True

def show_help():
    global turns_left
    turns_left = turns_left + 1
    print("Commands: look, go <location>, buy <item>, use <item>, inv, help, quit")

def show_location():
    global current_location
    print(f"\nYou are at {current_location}.")
    global money
    global moz_points
    global turns_left
    # describe based on location
    if current_location == "school":
        print("You're working as a teacher so you can afford to take mozzarella the maltipoo on adventures.")
        money = money + 3
        print("Your now on the road, you can go anywhere, even back to where you just were.")
        current_location = "road"
    elif current_location == "starbucks":
        if money < 5:
            turns_left = turns_left + 1
            print(f"Sorry you need at least $5 to go to starbucks, your balance is ${money}")
        else:
            print("your at starbucks working on your code while mozzarella the maltipoo is eatting tons of pup cups.")
            moz_points = moz_points + 1
            random_number = random.randint(1, 20)
            if random_number == 20:
                random_number2 = random.randint(5, 100)
                print(f"You finished your code and sold code to a client and made ${random_number2}")
                money = money + random_number2
                print("Your now on the road, you can go anywhere, even back to where you just were.")
                current_location = "road"
            else:
                money = money - 5
                print("Your now on the road, you can go anywhere, even back to where you just were.")
                current_location = "road"
    elif current_location == "cinemark":
        print('your at the lobby, you need to have a ticket to see the minecraft movie, mozzarella the gets in free though if you buy a ticket for $10, to buy a ticket type "buy ticket" to use a ticket type "use ticket" ')
    elif current_location == "park":
        print("you took mozzarella the maltipoo on a walk.")
        print("Your now on the road, you can go anywhere, even back to where you just were.")
        current_location = "road"
        moz_points = moz_points + 3
    else:
        turns_left = turns_left + 1
        print("You're wondering where to take mozzarella the maltipoo.")

def location_index(name):
    # map location name -> index in locations list (list practice; not using dict)
    for i, r in enumerate(locations):
        if r == name:
            return i
    return -1

def move_player(dest):
    global current_location
    global turns_left
    cur_idx = location_index(current_location)
    if cur_idx == -1:
        print("You feel lost in the woods...")
        return
    if dest in exits[cur_idx]:
        current_location = dest
        show_location()
    else:
        turns_left = turns_left + 1
        print("You can't go there from here.")

def use_item(item):
    global moz_points
    global current_location
    if current_location == "cinemark" and item == "ticket":
        print("You and mozzarella the maltipoo saw the minecraft movie")
        moz_points = moz_points + 100
        current_location = "home"
    if item == "steak":
        random_number3 = random.randint(10, 30)
        print(f"mozzarella the maltipoo liked the steak! you gained {random_number3} moz points!")
        moz_points = moz_points + random_number3
    else:
        print(f"no usable items at {current_location}")

def buy_item(item_name):
    global money
    global inventory
    global turns_left
    if item_name == "steak":
        if money >= 15:
            money -= 15
            inventory.append("steak")
            turns_left = turns_left + 1
            print(f"You bought a steak for $15. Your money is now ${money}.")
        else:
            print(f"You don't have enough money to buy a steak. You have ${money}, but it costs $15.")
    elif item_name == "ticket":
        if money >= 10:
            money -= 10
            inventory.append("ticket")
            turns_left = turns_left + 1
            print(f"You bought a ticket for $10. Your money is now ${money}.")
        else:
            print(f"You don't have enough money to buy a ticket. You have ${money}, but it costs $10.")
    else:
        print(f"Sorry, you can't buy {item_name}.")


def handle_command(cmd):
    parts = cmd.strip().lower().split()
    if not parts:
        return
    if parts[0] == "help":
        show_help()
    elif parts[0] == "look":
        show_location()
    elif parts[0] == "use" and len(parts) >= 2:
        use_item(parts[1])
    elif parts[0] == "go" and len(parts) >= 2:
        move_player(parts[1])
    elif parts[0] == "store":
        global turns_left
        turns_left = turns_left + 1
        print('type "buy steak" to buy a steak for $15, it will give somewhere from 10 to 30 moz points' \
        'type "buy ticket" to buy a ticket for $10 it will give 10 moz points when you use it at Cinemark')
    elif parts[0] == "buy" and len(parts) >= 2:
        buy_item(parts[1])
    elif parts[0] == "inv":
        print("Inventory:", inventory if inventory else "(empty)")
    elif parts[0] == "quit":
        global is_running
        is_running = False
    else:
        turns_left = turns_left + 1
        print("Unknown command. Type 'help'.")


# --- main loop ---
show_location()
if moz_points >= 69:
    has_won = True
else:
    while is_running and not has_won:
     # optional: pressure mechanic
     turns_left -= 1
     print(f"turns left = {turns_left}")
     print(f"Money = ${money}")
     print(f"Moz points = {moz_points}")
     if turns_left <= 0:
        print("\nmozzarella the maltipoo and you didn't finish the adventure. You lose.")
        break


     cmd = input("\n> ")
     handle_command(cmd)


if has_won:
    print("\nmozzarella the maltipoo is super happy now, you win!")
print("Game over.")
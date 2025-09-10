# Conditinal logic
# Operators ==, !=, >, <, >=, <=

num_1 = 10
num_2 = 20

def condition_check():
    if num_1 == 10: #True
        print(f"num_1 = {num_1}")

    if num_1 == 20: #False
        print(f"num_1 = {num_1}")

    elif num_1 < 20: #True
        print(f"num_1 is less then 20.")

    elif num_1 < num_2: #True
        print(f"num_1 is less then num_2.")
    else:
        print("Error Code Autism")

condition_check()
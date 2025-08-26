var_1 = input("Please enter your first number: ")
var_2 = input("Please enter your second number: ")
#adding these 2 numbers wont work because theyre strings. we must cast them to the correct datatype, a float.
var_1 = float(var_1)
var_2 = float(var_2)
#Addition

sum = var_1 + var_2
print(f"{var_1} + {var_2} = {sum}")

#subtraction
difference = var_1 - var_2
print(f"{var_1} - {var_2} = {difference}")

#multiplication
product = var_1 * var_2
print(f"{var_1} * {var_2} = {product}")

#division
quotient = var_1 / var_2
print(f"{var_1} / {var_2} = {quotient}")

# Power
power = var_1 ** var_2
print(f"{var_1} ** {var_2} = {power}")
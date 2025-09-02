print("Fuctions Below")


# How to Define a function
# start with def
# Indecation and spacing matters
x = 10
#call the sample function bellow
def sample_function():
    print(f"{x} You ran the fuction")
print(sample_function)


def do_addition(x, y):
    sum = x + y
    print(sum)

do_addition(3,10)
# Take input from the user and pass that value through the function
num_1 = float(input("Please enter a number:"))
num_2 = float(input("Please enter another number:"))

do_addition(num_1, num_2)
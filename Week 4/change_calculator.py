og_money = int(input("Give me monies in the value of pennys, IE. $1.24 = ¢124, enter here: ¢"))
money = og_money

hundred_bills = money / 10000
hundred_bills = int(hundred_bills)
money = money - hundred_bills * 10000

fifty_bills =  money/5000
fifty_bills = int(fifty_bills)
money = money - fifty_bills * 5000

twenty_bills =  money/2000
twenty_bills = int(twenty_bills)
money = money - twenty_bills * 2000

ten_bills =  money/1000
ten_bills = int(ten_bills)
money = money - ten_bills * 1000

five_bills =  money/500
five_bills = int(five_bills)
money = money - five_bills * 500

two_bills =  money/200
two_bills = int(two_bills)
money = money - two_bills * 200

one_bills =  money/100
one_bills = int(one_bills)
money = money - one_bills * 100

half_dollar =  money/50
half_dollar = int(half_dollar)
money = money - half_dollar * 50

quarter =  money/25
quarter = int(quarter)
money = money - quarter * 25

dimes =  money/10
dimes = int(dimes)
money = money - dimes * 10

nickle =  money/5
nickle = int(nickle)
money = money - nickle * 5

pennies =  money/1
pennies = int(pennies)
money = money - pennies * 1

print(half_dollar, quarter, dimes, nickle, pennies)

print(f"Change for ¢{og_money} is {hundred_bills} One Hundred dollar bills, {fifty_bills} fifty dollar bills, {twenty_bills} twenty dollar bills, {ten_bills} ten dollar bills, {five_bills} five dollar bills, {two_bills} two dollar bills, {one_bills} one dollar bills, {half_dollar} half dollar coins, {quarter} quarters, {dimes} dimes, {nickle} nickles, and {pennies} pennies.")
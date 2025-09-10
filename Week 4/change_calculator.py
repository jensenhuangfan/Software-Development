og_money = int(input("Give me monies no change yet $"))
money = og_money

hundred_bills = money / 100
hundred_bills = int(hundred_bills)
money = money - hundred_bills * 100

fifty_bills =  money/50
fifty_bills = int(fifty_bills)
money = money - fifty_bills * 50

twenty_bills =  money/20
twenty_bills = int(twenty_bills)
money = money - twenty_bills * 20

ten_bills =  money/10
ten_bills = int(ten_bills)
money = money - ten_bills * 10

five_bills =  money/5
five_bills = int(five_bills)
money = money - five_bills * 5

two_bills =  money/2
two_bills = int(two_bills)
money = money - two_bills * 2

one_bills =  money/1
one_bills = int(one_bills)
money = money - one_bills * 1

print(hundred_bills, fifty_bills, twenty_bills, ten_bills, five_bills, two_bills, one_bills)

og_cents = int(input("Give me cents no dollars ¢"))
cents = og_cents

half_dollar =  cents/50
half_dollar = int(half_dollar)
cents = cents - half_dollar * 50

quarter =  cents/25
quarter = int(quarter)
cents = cents - quarter * 25

dimes =  cents/10
dimes = int(dimes)
cents = cents - dimes * 10

nickle =  cents/5
nickle = int(nickle)
cents = cents - nickle * 5

pennies =  cents/1
pennies = int(pennies)
cents = cents - pennies * 1

print(half_dollar, quarter, dimes, nickle, pennies)
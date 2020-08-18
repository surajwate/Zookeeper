amount = int(input())
year = 0

while 50000 <= amount <= 700000:
    interest = amount * 0.071
    amount += interest
    year += 1

print(year)

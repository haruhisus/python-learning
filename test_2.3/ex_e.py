total = 0
while (price := float(input())) != 0:
    total += price - price / 10 if price >= 500 else + price
print(total)
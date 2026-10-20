count = 1
for i in range(1, int((num := int(input())) ** 0.5) + 1):
    count += 1 if num % i == 0 and num != 1 else 0
print("YES" if count == 2 else "NO")

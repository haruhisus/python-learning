count = 0
while (string := input()) != "Приехали!":
    if "зайка" in string:
        count += 1
print(count)


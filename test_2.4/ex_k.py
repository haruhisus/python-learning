for _ in range(count := int(input())):
    if (num := int(input())) == 1:
        count -= 1
        continue
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            count -= 1
            break
print(count)
    
num_max = int(input())
num = 0
for i in range(num_max + 1):
    for j in range(i + 1):
        num += 1
        print(num, end=' ')
        if num == num_max:
            break
    if num == num_max:
        break
    print()

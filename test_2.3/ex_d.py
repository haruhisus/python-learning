num_1, num_2 = int(input()), int(input())
step = 1 if num_1 <= num_2 else -1
for i in range(num_1, num_2 + step, step):
    print(i, end=' ')
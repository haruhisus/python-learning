N, M = int(input()), int(input())

for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(f"{i * j:^{M}}", end='|' if j < N else '\n')
    if i < N:
        print("-" * (M * N + N - 1))
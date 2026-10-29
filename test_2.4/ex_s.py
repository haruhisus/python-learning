N = int(input())
width = len(str((N + 1) // 2))
for i in range(N):
    for j in range(N):
        print(f"{min(i + 1, j + 1, N - i, N - j):>{width}}", end=" " if j < N - 1 else "\n")
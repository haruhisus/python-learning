N, M = int(input()), int(input())
width = len(str(N * M))
for i in range(1, N + 1):
    for j in range(M):
        print(f"{i + N * j:>{width}}", end=' ' if j < M - 1 else '\n')
N, M = int(input()), int(input())
width = len(str(N * M))
for i in range(1, N + 1):
    for j in range(M):
        if j % 2 != 0:
            print(f"{(j + 1) * N - i + 1:>{width}}", end=' ' if j < M - 1 else '\n')
        else:
            print(f"{i + N * j:>{width}}", end=' ' if j + 1 < M else '\n')
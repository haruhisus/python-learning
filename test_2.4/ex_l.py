N, M = int(input()), int(input())
width = len(str(N * M))
for i in range(N):
    for j in range(1, M + 1):
        print(f"{i * M + j:>{width}}", end=' ' if j < M else '\n')
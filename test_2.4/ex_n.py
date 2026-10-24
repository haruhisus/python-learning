N, M = int(input()), int(input())
width = len(str(N * M))
for i in range(N):
    for j in range(1, M + 1):
        if i % 2 == 0:
            print(f"{j + i * M:>{width}}", end=" " if j < M else "\n")
        else:
            print(f"{(i + 1) * M - j + 1:>{width}}", end=" " if j < M else "\n")
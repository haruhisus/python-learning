N, M, K1, K2 = int(input()), int(input()), int(input()), int(input())
x1 = N * (M - K1) // (K2 - K1)
x2 = N - x1
print(x1, x2)
N = int(input())
h_prev = 0
count = 0
while count != N:
    b = int(input())
    r = b // 256 % 256
    m = b // 256 ** 2
    h = b % 256
    if h != (37 * (m + r + h_prev)) % 256 or h >= 100:
        print(count)
        count = N
    elif count == N - 1:
        print(-1)
        count = N
    else:
        count += 1
        h_prev = h
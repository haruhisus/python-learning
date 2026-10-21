N = int(input())
h_pre = 0
count = 0
go = True
while go:
    b = int(input())
    r = b // 256 % 256
    m = b // 256 ** 2
    h = b % 256
    if h != (37 * (m + r + h_pre)) % 256 or h >= 100:
        print(count)
        go = False
    elif count == N - 1:
        print(-1)
        go = False
    else:
        count += 1
        h_pre = h

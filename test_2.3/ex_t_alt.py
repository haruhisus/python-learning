h_prev = 0
fake_block = 0
flag = True
for i in range(int(input())):
    b = int(input())
    r = b // 256 % 256
    m = b // 256 ** 2
    h = b % 256
    if (h != (37 * (m + r + h_prev)) % 256 or h >= 100) and flag:
        fake_block = i
        flag = False
    else:
        h_prev = h
print(-1 if flag else fake_block)
    
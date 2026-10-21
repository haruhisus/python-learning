h_prev = 0
fake_block = -1
for i in range(int(input())):
    b = int(input())
    r = b // 256 % 256
    m = b // 256 ** 2
    h = b % 256
    if (h != (37 * (m + r + h_prev)) % 256 or h >= 100) and fake_block == -1:
        fake_block = i
    elif fake_block == -1:
        h_prev = h
print(fake_block)   
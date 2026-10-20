num = int(input())
de = 2

while num // de > 1:
    if num % de == 0:
        print(de, end=' * ')
        num //= de
    else:
        de += 1
print(num)
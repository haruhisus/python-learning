num = int(input())
de = 2

while num > 1:
    if num % de == 0:
        print(de, end='')
        num //= de
        print(" * " if num != 1 else "", end='')
    else:
        de += 1
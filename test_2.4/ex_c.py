num_max = int(input())
col = row = num = 1

while num <= num_max:
    while col <= row and num <= num_max:
        print(num, end=' ')
        num += 1
        col += 1
    print()
    col = 1
    row += 1
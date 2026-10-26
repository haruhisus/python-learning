num_max = rest = int(input())
row = num = 1
k = 0

while rest > k + 1:
    k += 1
    rest -= k

width = rest - 1
for i in range(num_max - rest + 1, num_max + 1):
    width += len(str(i))

while num <= num_max:
    col = 1
    row_value = ""
    while col <= row and num <= num_max:
        row_value += str(num) + ("" if col == row or num == num_max else " ")
        num += 1
        col += 1
    print(f"{row_value:>{(width - len(row_value)) // 2 + len(row_value)}}")
    row += 1

count = 0
for _ in range(int(input())):
    flag = False
    while (string := input()) != 'ВСЁ':
        if string == "зайка":
            flag = True
    count += flag
print(count)
answer = ""
a, b = 0, 1001
while answer != "Угадал!":
    c = (a + b) // 2
    print(c)
    answer = input()
    match answer:
        case 'Больше':
            a = c
        case 'Меньше':
            b = c

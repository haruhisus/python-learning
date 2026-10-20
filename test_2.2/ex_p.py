speed_1, speed_2, speed_3 = int(input()), int(input()), int(input())

name_1, name_2, name_3 = "Петя", "Вася", "Толя"

if speed_1 < speed_2:
    name_1, name_2 = name_2, name_1
    speed_1, speed_2 = speed_2, speed_1

if speed_2 < speed_3:
    name_2, name_3 = name_3, name_2
    speed_2, speed_3 = speed_3, speed_2

if speed_1 < speed_2:
    name_1, name_2 = name_2, name_1
    speed_1, speed_2 = speed_2, speed_1

print(f"{name_1:^24}\n{name_2:^8}\n{name_3:>22}\n{'II':^8}{'I':^8}{'III':^8}")
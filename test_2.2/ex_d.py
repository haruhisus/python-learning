name1, name2, name3 = "Петя", "Вася", "Толя"
speed1, speed2, speed3 = int(input()), int(input()), int(input())

if speed1 < speed2:
    speed1, speed2 = speed2, speed1
    name1, name2 = name2, name1
if speed2 < speed3:
    speed2, speed3 = speed3, speed2
    name2, name3 = name3, name2
if speed1 < speed2:
    name1, name2 = name2, name1

print(f"1. {name1}\n2. {name2}\n3. {name3}")
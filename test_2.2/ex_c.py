petya, vasya, tolya = int(input()), int(input()), int(input())
if petya > vasya and petya > tolya:
    print("Петя")
elif vasya > petya and vasya > tolya:
    print("Вася")
else:
    print("Толя")
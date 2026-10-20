a, b, c = int(input()), int(input()), int(input())

if min(a, b, c) ** 2 + (a + b + c - max(a, b, c) - min(a, b, c)) ** 2 == max(a, b, c) ** 2:
    print("100%")
elif min(a, b, c) ** 2 + (a + b + c - max(a, b, c) - min(a, b, c)) ** 2 < max(a, b, c) ** 2:
    print("велика")
else:
    print("крайне мала")
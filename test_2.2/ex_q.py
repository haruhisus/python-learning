a, b, c = float(input()), float(input()), float(input())

if a == 0 and b == 0 and c == 0:
    print("Infinite solutions")
elif a == 0 and b == 0:
    print("No solution")
elif a == 0:
    x_1 = -c / b
    print(f"{x_1:.2f}")
else:
    D = b ** 2 - 4 * a * c
    if D > 0:
        x_1 = (-b + D ** 0.5) / (2 * a)
        x_2 = (-b - D ** 0.5) / (2 * a)
        print(f"{min(x_1, x_2):.2f} {max(x_1, x_2):.2f}")
    elif D == 0:
        x_1 = (-1 * b + D ** 0.5) / 2 * a
        print(f"{x_1:.2f}")
    elif D < 0:
        print("No solution")

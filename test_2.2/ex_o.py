num1, num2 = int(input()), int(input())

a = num1 // 10
b = num1 % 10
c = num2 // 10
d = num2 % 10

print(f"{max(a, b, c, d)}{(a + b + c + d - max(a, b, c, d) - min(a, b, c, d)) % 10}{min(a, b, c, d)}")
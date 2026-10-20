num = int(input())

a = num // 100
b = num // 10 % 10
c = num % 10

if min(a, b, c) != 0:
    min_num = int(str(f"{min(a, b, c)}{a + b + c - min(a, b, c) - max(a, b, c)}"))
else:
    min_num = int(str(f"{a + b + c - min(a, b, c) - max(a, b, c)}{min(a, b, c)}"))
    
max_num = int(str(f"{max(a, b, c)}{a + b + c - min(a, b, c) - max(a, b, c)}"))

print(f"{min_num} {max_num}" if min_num // 10 != 0 else f"{max_num} {max_num}")
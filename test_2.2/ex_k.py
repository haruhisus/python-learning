num = int(input())

a = num // 100
b = num // 10 % 10
c = num % 10

num_max = max(a, b, c)
num_min = min(a, b, c)
num_mid = a + b + c - num_max - num_min

print("YES" if num_max + num_min == num_mid * 2 else "NO")
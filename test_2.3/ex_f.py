a, b = int(input()), int(input())

while b:
    a, b = b, a % b
print(a)

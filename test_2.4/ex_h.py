sum_w = 0
name_w = ""
for _ in range(int(input())):
    name = input()
    num = int(input())
    sum = 0
    while num:
        sum += num % 10
        num //= 10
    if sum >= sum_w:
        sum_w = sum
        name_w = name
print(name_w)
    

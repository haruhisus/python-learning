sl = num_sum_max = 0
num = int(input())
for i in range(10, 1, -1):
    num_sum = 0
    num_sl = num
    while num_sl:
        num_sum += num_sl % i
        num_sl //= i
    if num_sum >= num_sum_max:
        num_sum_max = num_sum
        sl = i
print(sl)
num = int(input())

sum1 = num // 10 % 10 + num % 10
sum2 = num // 100 + num // 10 % 10

print(f"{sum1}{sum2}" if sum1 >= sum2 else f"{sum2}{sum1}")
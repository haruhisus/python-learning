num1, num2 = int(input()), int(input())
print(int(f"{(num1 // 100 + num2 // 100) % 10}{(num1 // 10 + num2 // 10) % 10}{(num1 + num2) % 10}"))
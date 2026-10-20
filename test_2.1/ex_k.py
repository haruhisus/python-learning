number = int(input())
print(f"{number // 100 % 10}{number // 1000}", end='')
print(f"{number % 10}{number // 10 % 10}")
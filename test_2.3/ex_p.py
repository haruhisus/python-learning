num_original = num = int(input())
num_reverse = 0

while num:
    num_reverse = num_reverse * 10 + num % 10
    num //= 10
print("YES" if num_original == num_reverse else "NO")
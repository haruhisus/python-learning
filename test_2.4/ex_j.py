slices = int(input())
print("А Б В")
for i in range(1, slices - 1):
    for j in range(1, slices - i):
            print(i, j, slices - i - j)

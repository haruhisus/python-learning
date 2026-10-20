product, price, weight, cash = input(), int(input()), int(input()), int(input())
print(f"Чек\n{product} - {weight}кг - {price}руб/кг\nИтого: {price * weight}руб")
print(f"Внесено: {cash}руб\nСдача: {cash - price * weight}руб")
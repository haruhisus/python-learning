x = y = 0
while (command := input()) != "СТОП":
    steps = int(input())
    match command:
        case 'СЕВЕР':
            y += steps
        case 'ЮГ':
            y -= steps
        case 'ЗАПАД':
            x -= steps
        case 'ВОСТОК':
            x += steps
print(y, x, sep='\n')
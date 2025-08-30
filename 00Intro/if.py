print("----------------")
print("Початок програми")
a = 3
b = 94

#if 1
if a > b or c == True:
    print(f"1. Число {a}")
if b > a or c == True:
    print(f"1. Число {a}")

#if 2
if b == 1000:
    print(f"2. Число b={b} (1000)")

elif a > b or c == True:
    print(f"2. Число а={a}")
elif b > a or c == True:
    print(f"2. Число b={b}")

print("Кінець програми")
print("----------------")


temperature = 28
isRaining = False

if temperature > 30:
    if isRaining:
        print("Жарко і дощ")
    else:
        print("Жарко")
elif temperature > 20:
    if isRaining:
        print("Тепло і дощ")
    else:
        print("Тепло")
else:
    print("Холодно")


# Оператор match

day: str = input('Введіть день: ')
day = day.capitalize()

match day:
    case"Monday":
        print("Початок робочого тижня")        # оператор pass заповнювач, не робить нічого
    case "tuesday":
        pass
    case "wednesday":
        print("Середина")
    case "thursday":
        pass
    case "friday":
        print("Кінець робочого тижня")
    case "saturday":
        pass
    case "sunday":
        pass
import json
import os

FILENAME = 'menu.json'

if os.path.exists(FILENAME):
    with open(FILENAME, 'r', encoding="utf-8") as f:
        menu = json.load(f)
else:
    menu = {
        'Піца': ['тісто', 'сир', 'ковбаса'],
        'Салат': ['огірок', 'помідор', 'олія']
    }
print('Вітаємо в ресторані!')

while True:
    print('-'*40)
    action = input("Введи: 1-перегляд, 2-додати, 3-стоп: ")

    if action == 'стоп' or action == '3':
        with open(FILENAME, 'w', encoding="utf-8") as f:
            json.dump(menu, f, ensure_ascii=False, indent=4)
        print("Мень збережено")
        break

    if action == '1' or action == 'перегляд':
        for dish in menu:
            print('Страва: ', dish)
            print('Інгредієнти: ')
            for ing in menu[dish]:
                print('-', ing)

    elif action == '2' or action == 'додати':
        new_dish = input('Введи назву нової страви: ')
        ingredients = []
        print("Вводь інгредієнти (1/стоп щоб закінчити): ")

        while True:
            ing = input("Інгредієнти: ")
            if ing == '1' or ing == 'стоп':
                break
            ingredients.append(ing)

        menu[new_dish] = ingredients
        print("Страву додано!")
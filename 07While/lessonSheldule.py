import json
import os

FILENAME = 'menu.json'

if os.path.exists(FILENAME):
    with open(FILENAME, 'r', encoding="utf-8") as f:
        schedole = json.load(f)
else:
    schedole = {
        'Понеділок': ['Математика', 'Фізика', 'Історія'],
        'Вівтрок': ['Геометрія', 'Англійська', 'Хімія']
    }

print("Вітаємо на Нові знання")

while True:
    print('-'*40)
    action = input("Введи: 1-перегляд, 2-додати, 3-редагувати, 4-стоп: ")


#словник товарів: назва -> ціна

products = {"яблуко":6, "хліб":25, "молоко":30, "шоколад":60}

cart = []
total = 0

print("Магазин продуктів:")
for name in products:
    print('-', name, ':', products[name], 'грн')

print('-'*50)

while True: # ! безкінечний цикл
    choice = input("Введіть товар(або стоп для вихлду):")

    if choice == 'стоп':
        break

    if choice in products:
        price = products[choice]
        cart.append((choice, price))
        total += price
        print('Додано: ', choice, '-', price, 'грн')
    else:
        print("Такого товару нема")

print('Ваші покупки: ')
for item in cart:
    print(item[0], '-', item[1], 'грн')

print('Загальна сума: ', total)
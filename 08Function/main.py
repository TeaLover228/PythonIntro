# функції
#
#def functionName():
#    # ...
#    # тіло функції
#    # ...
#
#    return # ? результат

# 1. функція без параметрів
def hello():
    # 1 ...
    print('Привіт це функція')

hello()

# 2. функція з параметром
def greet(name):
    print("Пивіт", name)

greet('Mike')

# 3. функція з параметром за замовчуванням
def greetV2(name="користувач"):
    print(f"Привт {name}")

greetV2()
greetV2('Василь')

# 4.
def userInfo(name:str, age:int = 0, email:str = '') -> str:
    """
    Функція оримання даних по користувачу
    :param name: Імя користувача
    :param age: Вік користувачв
    :param email: Адреса користувача
    :return: Статус користувача
    """

    result:str = ''
    # код функції

    if age > 16:
        result += "Дослий"
    else:
        result += "Неповнолітній"

    return result

# - 1
print(userInfo("Петро", 20))
# - 2
s = userInfo(age = 20, name = "Петро")
print(s)


# довільна кількість параметрів

def sumNumbers(*args):
    sum = 0
    for s in args:
        sum += s

    return sum

print(sumNumbers(2, 4, 5, 4, 4, 4))







































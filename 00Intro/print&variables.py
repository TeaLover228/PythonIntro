# вступ/повторення

name: str = "Michael"
isStudent: bool = False
age: int = 21
grade: int = 76.54

print('Інформація по користувачу')

# 1 простий вивід
print(name, isStudent, age, grade)

# 2 з текстом пояснення
print(' Імя:', name, ' Студент:', isStudent, ' Вік', age, ' Оцінка:', grade, sep="")

# 3 форматований текст
print(f"Імя:{name} Студент:{isStudent} Вік:{age} Оцінка:{grade}")

# 4 форматуючий символ
print(f"Імя:%s Студент:%s Вік:%d Оцінка:%f" % (name, isStudent, age, grade))

# -------------------------------------------------------------------------------
# введення значень
number1 = int(input('Введіть число 1:'))
number2 = int(input('Введіть число 2:'))

print(f"Сума чисел {number1} + {number2} =", number1 + number2)

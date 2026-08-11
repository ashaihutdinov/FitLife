# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30
ML_IN_LITER = 1000

user_name = input("Введите ваше имя: ")

while True:
    try:
        user_age = int(input("Введите возраст: "))
        break
    except ValueError:
        print("Введите цифры, не буквы")

while True:
    try:
        user_weight = float(input("Введите вес (в кг): "))
        break
    except ValueError:
        print("Введите цифры, не буквы")

while True:
    try:
        user_height = float(input("Введите рост в метрах, пример 1.75): "))
        break
    except ValueError:
        print("Введите цифры, не буквы")

bmi = round(user_weight / (user_height ** 2), 1)

water_liters = user_weight * WATER_PER_KG / ML_IN_LITER

print(f"Отчет для пользователя: {user_name} ({user_age} г.)")
print(f"Твой Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_liters:.1f} л. в день")
print()
print("Расчет окончен. Будьте здоровы!")

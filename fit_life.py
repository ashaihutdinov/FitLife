# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30
ML_IN_LITER = 1000


user_name = input("Введите ваше имя: ")
user_age = int(input("Введите ваш возраст: "))


user_weight = float(input("Введите ваш вес (в кг): "))
user_height = float(input("Введите ваш рост (в метрах, например 1.75): "))


bmi = round(user_weight / (user_height ** 2), 1)


water_needed = user_weight * WATER_PER_KG

water_liters = water_needed / ML_IN_LITER


print(f"Отчет для пользователя: {user_name} ({user_age} г.)")
print(f"Твой Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_liters:.1f} л. в день")
print()
print("Расчет окончен. Будьте здоровы!")

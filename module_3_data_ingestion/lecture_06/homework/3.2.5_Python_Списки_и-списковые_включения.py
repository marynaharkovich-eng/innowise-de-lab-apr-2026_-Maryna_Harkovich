# --Задание 1 ---
# 1. Инициализировать данные:
rows_range = range(1, 6)
rows = list(rows_range)

# 2. Выполнить изменение по индексу:
rows[2] = "Ремонт"

# 3. Проверить наличие значения:
if 5 in rows:
    print("Ряд 5 доступен")

# 4.  Выполнить срез:
priority_rows = rows[:3]

# 5.  Выполнить срез:
print(f"Список рядов: {rows}")
print(f"Приоритетные ряды: {priority_rows}")

# --Задание 2 ---
# 1. Инициализировать список prices со следующими значениями в коде:
prices = [100, -50, 300, 40, 800]

# 2. Очистить данные:
prices.remove(-50)

# 3. Изменить список:
prices.append(150)

# 4.Отсортировать список:
prices.sort()

# 5. Создать новый список через List Comprehension:
# Формула: цена * 1.2, если результат > 100
tax_prices = [p * 1.2 for p in prices if p * 1.2 > 100]

# 6. Вывести в консоль:
print(f"Базовый прайс (очищенный): {prices}")
print(f"Цены с НДС (>100): {tax_prices}")
print(f"Общая выручка: {sum(tax_prices)}")
print(f"Минимум: {min(tax_prices)}")
print(f"Максимум: {max(tax_prices)}")
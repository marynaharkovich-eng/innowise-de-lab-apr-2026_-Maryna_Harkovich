# Задание 1
products = ["Яблоки", "Хлеб", "Молоко", "Печенье", "Сок", "Кефир"]
for i in range(0, len(products), 2):
    product_name = products[i]
    name_length = len(product_name)
    
    
    if product_name == "Бананы":
        print(f"Обнаружены Бананы! Проверка прервана экстренно.")
        break
    
   
    print(f"Индекс {i}: Проверен товар {product_name} (Длина названия: {name_length} символов)")

else:
    print("--- Выборочная проверка успешно завершена ---") 

# Задание 2


daily_logs = [
    [500, 0, 1200],       # Касса 1
    [300, -999, 800],     # Касса 2 (сбой на -999)
    [1500, 200]           # Касса 3
]

total_revenue = 0

# Внешний цикл: перебираем кассы
# enumerate дает индекс (начиная с 0) и сам список транзакций
for index, cash_register in enumerate(daily_logs, start=1):
    print(f"--- Обработка Кассы №{index} ---")
    
    # Внутренний цикл: перебираем транзакции в текущей кассе
    for transaction in cash_register:
        
        # 1. Проверка на аварийную остановку
        if transaction == -999:
            print("Аварийная остановка кассы!")
            break  # Прерывает только текущую кассу, переходим к следующей
            
        # 2. Проверка на технический сбой (0)
        elif transaction == 0:
            print("Пропуск сбоя")
            continue  # Пропускаем остаток кода в этом шаге, идем к след. транзакции
            
        # 3. Обработка успешной транзакции
        elif transaction > 0:
            total_revenue += transaction
            print(f"Добавлено: {transaction}")

# Итоговый вывод после всех циклов
print("=== ИТОГ ДНЯ ===")
print(f"Общая выручка магазина: {total_revenue}")
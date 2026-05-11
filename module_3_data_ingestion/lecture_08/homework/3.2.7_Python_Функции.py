# ---Задание 1---
SMALL_BATCH_LIMIT = 500

def calculate_batch(weight, price, discount=0.0):
    """
    Рассчитывает финальную стоимость партии товара и проверяет превышение лимита.

    Args:
        weight (float): Вес товара.
        price (float): Цена за единицу.
        discount (float): Скидка в виде десятичной дроби (0.10 = 10%). По умолчанию 0.0.

    Returns:
        tuple: (final_sum, is_limit_exceeded)
    """
    total_sum = weight * price * (1 - discount)
    is_limit_exceeded = total_sum > SMALL_BATCH_LIMIT
    
    return total_sum, is_limit_exceeded

# Вызов 1: Морковь (100 кг по 4$)
sum_carrot, limit_carrot = calculate_batch(100, 4)

# Вызов 2: Яблоки (50 кг по 20$, скидка 10%)
sum_apple, limit_apple = calculate_batch(50, 20, discount=0.1)

# Вывод отчета
print(f"Партия 1 (Морковь): Сумма {sum_carrot}. Превышение лимита: {limit_carrot}")
print(f"Партия 2 (Яблоки): Сумма {sum_apple}. Превышение лимита: {limit_apple}")

# ---Задание 2---
def audit_logger(func):
    """Декоратор, который логирует запуск и завершение функции."""
    def wrapper(*args, **kwargs):
        print("[AUDIT] Запуск анализа...")
        result = func(*args, **kwargs)
        print("[AUDIT] Анализ завершен.")
        return result
    return wrapper

@audit_logger
def get_sorted_report(data):
    """
    Сортирует список филиалов по выручке в порядке убывания.
    """
    # Сортировка с использованием lambda-функции
    return sorted(data, key=lambda x: x['revenue'], reverse=True)

branches = [
    {"city": "Minsk", "revenue": 15000},
    {"city": "Warsaw", "revenue": 32000},
    {"city": "London", "revenue": 12000}
]

# Получение результата
sorted_branches = get_sorted_report(branches)

print("Топ филиалов:")
for index, branch in enumerate(sorted_branches, 1):
    print(f"{index}. {branch['city']}: {branch['revenue']}")
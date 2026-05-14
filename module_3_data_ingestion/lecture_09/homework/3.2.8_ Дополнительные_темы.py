# ---Задание_1---
def calculate_purchase(product_name: str, weight: any, price: float) -> None:
    """
    Рассчитывает стоимость партии товара и технический индекс.
    
    :param product_name: Название товара
    :param weight: Вес партии (ожидается число или строка-число)
    :param price: Цена за кг
    """
    try:
        # Попытка конвертации и расчетов
        numeric_weight = float(weight)
        total_cost = numeric_weight * price
        technical_index = 100 / numeric_weight
        
        print(f"Товар: {product_name}. Итоговая стоимость: {total_cost}$")

    except TypeError as e:
        print(f"Тип ошибки: {type(e)}")
        print(f"Сообщение: {e}")
        
    except ValueError as e:
        print(f"Тип ошибки: {type(e)}")
        print(f"Сообщение: {e}")
        
    except ZeroDivisionError as e:
        print(f"Тип ошибки: {type(e)}")
        print(f"Сообщение: {e}")

    finally:
        print("--- Проверка партии завершена ---")
        print()  # Пустая строка для читаемости вывода

# Тестирование функции
if __name__ == "__main__":
    # 1. Корректные данные
    calculate_purchase("Томаты", 100, 2.5)

    # 2. Ошибка значения (ValueError)
    calculate_purchase("Огурцы", "пятьдесят", 1.8)

    # 3. Ошибка деления на ноль (ZeroDivisionError)

    calculate_purchase("Перец", 0, 4)

    # 4. Ошибка типа данных (TypeError)
    calculate_purchase("Зелень", [10], 5)

   
    # ---Задание 2---
from typing import Union, Optional, Sequence
def calculate_total_delivery_cost(
    product_name: str,
    weights: list[float] | tuple[float, ...],
    prices: list[float] | tuple[float, ...],
    discount: float | None = None,
    currency_rate: int | float = 1,
    *extra_costs: float
) -> dict[str, float]:
    """
    Рассчитывает полную стоимость доставки с учетом скидок, налогов и доп. расходов.

    :param product_name: Название партии товара.
    :param weights: Список или кортеж с весами.
    :param prices: Список или кортеж с ценами.
    :param discount: Процент скидки (0.1 = 10%) или None.
    :param currency_rate: Коэффициент валюты.
    :param extra_costs: Прочие расходы (доставка, упаковка и т.д.).
    :return: Словарь с названием товара и итоговой суммой.
    """
    
    if len(weights) != len(prices):
        raise ValueError("Количество элементов в списках весов и цен должно совпадать.")

    # Типизация локальных переменных
    total_sum: float = 0.0
    
    # Расчет базовой стоимости
    for i in range(len(weights)):
        total_sum += weights[i] * prices[i]
    
    # Применение скидки
    if discount is not None:
        discount_sum: float = total_sum * (1 - discount)
        total_sum = discount_sum
    
    # Добавление экстра-расходов
    extra_sum: float = sum(extra_costs)
    total_sum += extra_sum
    
    # Учет курса валют
    final_sum: float = total_sum * currency_rate
    
    return {product_name: round(final_sum, 2)}

# Тестирование функции
if __name__ == "__main__":
    # 1. Овощная партия
    veg_result = calculate_total_delivery_cost(
        "Овощная партия", 
        [100, 50], 
        [4, 6], 
        0.1, 
        1, 
        20, 15
    )
    print(f"Товар: {list(veg_result.keys())[0]}, итоговая стоимость: {veg_result['Овощная партия']}")

    # 2. Фруктовая партия
    fruit_result = calculate_total_delivery_cost(
        "Фруктовая партия", 
        (30, 20, 10), 
        (15, 12, 18), 
        None, 
        1.2, 
        25
    )
    print(f"Товар: {list(fruit_result.keys())[0]}, итоговая стоимость: {fruit_result['Фруктовая партия']}")
# ---Задание 1 ---
# 1. Создание кортежа
center_coords = (40.7128, -74.0060)

# 2. Попытка изменения (вызовет TypeError)
# center_coords[0] = 41.0000 

# 3. Вывести сообщение:
print(f"Coordinates of the location of the central warehouse: {center_coords[0]} , {center_coords[1]}")

# 4. Проверить и вывести на экран:
print(type(center_coords))
print(len(center_coords))

# ---Задание 2 ---
# 1. Создать словарь product.
product = { 
    "id": 105, 
    "name": "Organic Buckwheat", 
    "price": 3.50, 
    "stock": 100 
}

# 2. Изменить значение ключа
product["price"] = 4.20

# 3. Добавить новый ключ
product["category"] = "Grains"

# 4. Используя .get(), попытаться получить ключ
# Если ключа "discount" нет, вернется 0
discount_rate = product.get("discount", 0)

# 5. Вывести на экран:
print(product)
print(discount_rate)

# ---Задание 3 ---

# 1.Входные данные
suppliers_log = [ 
    "FreshFarm Inc", 
    "GreenFields Ltd", 
    "AgroWorld Co", 
    "FreshFarm Inc", 
    "GreenFields Ltd" 
]

# 2. Преобразовать его в множество
unique_suppliers = set(suppliers_log)

# 3. Попробовать добавить нового поставщика "GreenFields Ltd".
unique_suppliers.add("GreenFields Ltd")

# 4.Проверить, есть ли "FreshFarm Inc" в множестве (использовать in).
is_present = "FreshFarm Inc" in unique_suppliers

# 5. Вывести:
print(is_present)
print(unique_suppliers)
print(len(unique_suppliers))

# ---Задание 4 ---
# 1 Входные данные
usd_prices = { 
    "Banana": 1.2, 
    "Mango": 2.5, 
    "Avocado": 2.0 
}

# 2. Пересчет в EUR через Dictionary Comprehension
eur_prices = {fruit: round(price * 0.9, 2) for fruit, price in usd_prices.items()}

# 3. Вывод
print(eur_prices)

# ---Задание 5 ---
# 1. Импортировать модуль json.
import json 

# 2. Создать переменную api_response_json (JSON-строка).
api_response_json = """ 
{ 
    "store": "StoreHub", 
    "orders": [ 
        {"id": 1, "total": 50}, 
        {"id": 2, "total": 200}, 
        {"id": 3, "total": 150} 
    ]
} 
"""

# 3. Преобразовать JSON в словарь Python с помощью json.loads().
data = json.loads(api_response_json)

# 4-5. Фильтрация заказов через List Comprehension
orders = data["orders"]
high_value_orders = [order for order in orders if order["total"] > 100]

# 6. Добавление нового ключа в словарь
data["high_value_orders"] = high_value_orders

# 7. СПреобразовать обновлённый словарь обратно в JSON-строку через json.dumps().

updated_json = json.dumps(data)

# 8. Вывод
print(updated_json)

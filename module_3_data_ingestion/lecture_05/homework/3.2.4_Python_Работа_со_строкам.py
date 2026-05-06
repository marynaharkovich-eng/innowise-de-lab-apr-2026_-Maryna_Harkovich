# --- ЗАДАНИЕ 1 ---

# 1. Входные данные
raw_log = "ORDER-2025-01-15|FRT-APPLE-PL|+111 (23) 456-78-90| мИНсК "

# Разделить строку, используя .split("|") и сохранить все части в переменные:order_id, product_code, raw_phone, raw_city
parts = raw_log.split("|")
order_id = parts[0]
product_code = parts[1]
raw_phone = parts[2]
raw_city = parts[3]

# 2. Разобрать код товара
category = product_code[:3]
region = product_code[-2:]
first_dash_pos = product_code.find("-")

print(f"Позиция первого дефиса в коде товара: {first_dash_pos}")

if product_code.startswith("FRT"):
    print("Код товара начинается с 'FRT'")
else:
    print("Код товара не начинается с 'FRT'")

# 3.  Поскольку телефон записан в разном формате, его необходимо привести к телефонному формату:
clean_phone = ""
for char in raw_phone:
    if char.isdigit():
        clean_phone += char

print(f"Длина номера телефона: {len(clean_phone)}")

# 4. Необходимо привести название города к нормальному виду, так как он введён с пробелами и разным регистром:
clean_city = raw_city.strip().lower().title()

# 5. Формирование итогового отчета
report = (
    f"Заказ: {order_id}\n"
    f"Категория: {category} | Регион: {region}\n"
    f"Телефон: {clean_phone}\n"
    f"Город: {clean_city}"
)

print(report)


# --- ЗАДАНИЕ 2 ---

# 1. Входные данные
product = " фермерский ТВОРОГ " 
price = 4.567 
qty = 3 
csv_row = "milk,bread,cheese" 
review = "Это лучший ТВОРОГ в городе!" 
# Путь к файлу с использованием raw-строки r""
file_path = r"C:\EcoMarket\data\2025\january\sales.csv"

# Нормализация названия товара:
clean_product = product.strip().lower().title()

# 2. Формирование чека для клиента
total = price * qty
# Округление до 2 знаков (.2f), \n - перенос, \t - табуляция
receipt = (
    f"Чек \"EcoMarket\"\n"
    f"\tТовар: {clean_product}\n"
    f"\tКол-во: {qty}\n"
    f"\tИтого: {total:.2f} руб."
)
print(receipt)

# 3. Подготовка строки из CSV
csv_list = csv_row.split(",")
formatted_csv = " | ".join(csv_list)
print(formatted_csv)

# 4. Проверка отзыва клиента
# Проверяем вхождение слова "творог" в нижнем регистре
if "творог" in review.lower():
    print("Отзыв относится к категории: Dairy")

# 5. Работа с путём к файлу
print(file_path)
# Задание 1
# 1. Инициализировать входные переменные.
raw_sku = "CARROT-001"
raw_regions = ("Minsk", "Warsaw", "Berlin", "Warsaw")
raw_weight_str = "2.5"
raw_stock_str = "150"
# 2. Выполнить явное преобразование типов:
weight_kg = float(raw_weight_str)
stock_quantity = int(raw_stock_str)
#3. Выполнить преобразование коллекций:
sku_as_list = list(raw_sku)
regions_list = list(raw_regions)
unique_regions = set(raw_regions)
regions_tuple = tuple(unique_regions)
#4. Создать пустые коллекции двумя способами, где это возможно:
empty_list_1 = []
empty_list_2 = list()

empty_dict_1 = {}
empty_dict_2 = dict()

empty_tuple_1 = ()
empty_tuple_2 = tuple()

empty_set = set()
# 5. Проверить “пустоту” коллекций через bool():
# Пустые
res_empty_list = bool(empty_list_1)
res_empty_dict = bool(empty_dict_1)
res_empty_tuple = bool(empty_tuple_1)
res_empty_set = bool(empty_set)

# Непустые (создаем без методов)
not_empty_list = [1]
not_empty_dict = {"a": 1}
not_empty_tuple = (1,)
not_empty_set = {1}

res_not_empty_list = bool(not_empty_list)
res_not_empty_dict = bool(not_empty_dict)
res_not_empty_tuple = bool(not_empty_tuple)
res_not_empty_set = bool(not_empty_set)
# 6. Вывести в консоль значения и типы:
print(weight_kg, type(weight_kg))
print(stock_quantity, type(stock_quantity))
print(sku_as_list, type(sku_as_list))
print(regions_list, type(regions_list))
print(unique_regions, type(unique_regions), regions_tuple, type(regions_tuple))

# Вывод bool для пустых
print(res_empty_list)
print(res_empty_dict)
print(res_empty_tuple)
print(res_empty_set)

# Вывод bool для непустых
print(res_not_empty_list)
print(res_not_empty_dict)
print(res_not_empty_tuple)
print(res_not_empty_set)


# Задание 2
#1. Создать исходные переменные товара.

product_name = "Морковь мытая"
price = 2.5
stock_quantity = 150
is_local_farm = True
supplier = None

has_coupon = True
has_card = False
total = 10
# 2. Рассчитать is_hit по правилу:
is_hit = price < 3 and is_local_farm

# 3. Вывести на экран
print(f"Является ли товар хитом? {is_hit}")

# 4.Добавить проверки (каждая проверка — отдельная переменная и вывод):
has_supplier = supplier is not None
print(f"Поставщик указан? {has_supplier}")

can_show_in_app = has_supplier and stock_quantity > 0
print(f"Показывать в приложении? {can_show_in_app}")

needs_restock = stock_quantity <= 20 or is_hit
print(f"Нужно пополнение? {needs_restock}")

is_blocked = not (is_local_farm)
print(f"Товар заблокирован для акции? {is_blocked}")

print() # Пустая строка для красоты вывода

# 5. Проверка приоритетов and/or
discount_without_brackets = has_coupon or has_card and total > 50
discount_with_brackets = (has_coupon or has_card) and total > 50

print(f"Скидка без скобок: {discount_without_brackets}")
print(f"Скидка со скобками: {discount_with_brackets}")

print()

# 6. Изменить значения с помощью расширенных операторов присваивания, затем повторить ключевые проверки:
price += 1.0
stock_quantity *= 2

boxes = stock_quantity
boxes //= 10

# Повторный расчет логики после изменений
is_hit_after = price < 3 and is_local_farm
needs_restock_after = stock_quantity <= 20 or is_hit_after

print(f"Цена после изменения: {price}")
print(f"Остаток после изменения: {stock_quantity}")
print(f"Полных коробок по 10 кг: {boxes}")
print()
print(f"Является ли товар хитом (после изменений)? {is_hit_after}")
print(f"Нужно пополнение (после изменений)? {needs_restock_after}")
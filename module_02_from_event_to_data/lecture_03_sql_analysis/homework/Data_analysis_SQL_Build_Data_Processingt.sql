--Задание 1: Работа с DML

-- 1. Вставить два новых Продукта (Products)
-- Используем ID 506 и 507, чтобы не дублировать существующие
INSERT INTO products (product_id, product_name, price, category_id, class, modify_timestamp, resistant, is_allergic, vitality_days)
VALUES 
(506, 'Eco Apple Juice', 5.50, 1, 'A', NOW()::varchar, 'Yes', 'No', 30),
(507, 'Gluten-Free Oats', 12.00, 2, 'B', NOW()::varchar, 'No', 'Yes', 180);

-- 2. Выбрать только Продукты, у которых is_allergic и resistant = 'Yes'
SELECT * FROM products 
WHERE is_allergic = 'Yes' 
  AND resistant = 'Yes';

-- 3. Обновить is_allergic для 'Bananas Family Pack' на 'Yes'
UPDATE products 
SET is_allergic = 'Yes' 
WHERE product_name = 'Bananas Family Pack';

-- 4. Удалить один из двух добавленных продуктов
-- Удаляем продукт с ID 506
DELETE FROM products 
WHERE product_id = 506;

-- 5. Проверить все изменения
SELECT * FROM products;

/*Задание 2: Работа с DDL
Цель: Практика создания и изменения структуры таблиц, управляющих пайплайнами данных.

Действия:

Создать новую таблицу с именем Data_Layers необходимую для описания слоев со столбцами: LayerID (SERIAL, PRIMARY KEY), LayerName (VARCHAR(50), UNIQUE, NOT NULL), Description (TEXT).
Заполнить колонку LayerName тремя значениями 'Bronze', 'Silver', 'Gold', которые обозначают слои в медальонной архитектуре.
Добавить колонку manager_email в таблицу Data_Layers (VARCHAR(100)).
Добавить ограничение UNIQUE к столбцу manager_email в таблице shops (предварительно заполнив столбец любыми значениями, чтобы избежать ошибки).
Переименовать столбец address в таблице Shops в shop_address.*/

-- 1. Создание таблицы Data_Layers
CREATE TABLE Data_Layers (
    LayerID SERIAL PRIMARY KEY,
    LayerName VARCHAR(50) UNIQUE NOT NULL,
    Description TEXT
);

-- 2. Заполнение колонки LayerName (Bronze, Silver, Gold)
INSERT INTO Data_Layers (LayerName, Description)
VALUES 
('Bronze', 'Raw data layer - landing zone for source data'),
('Silver', 'Cleaned and standardized data layer'),
('Gold', 'Business-ready aggregated data layer');

-- 3. Добавление колонки manager_email в таблицу Data_Layers
ALTER TABLE Data_Layers 
ADD COLUMN manager_email VARCHAR(100);

-- 4. Добавление UNIQUE email в таблицу shops
--  Сначала добавим саму колонку (если её нет)
ALTER TABLE shops ADD COLUMN IF NOT EXISTS manager_email VARCHAR(100);

-- Заполняем уникальными значениями, чтобы UNIQUE сработал без ошибок
UPDATE shops 
SET manager_email = 'manager' || shop_id || '@ecomarket.com';

--  Теперь накладываем ограничение UNIQUE
ALTER TABLE shops 
ADD CONSTRAINT unique_manager_email UNIQUE (manager_email);

-- 5. Переименование столбца address в shop_address
ALTER TABLE shops 
RENAME COLUMN address TO shop_address;

/*Задание 3: DCL (Управление доступом к данным)
Цель: Научиться создавать роли (пользователей) и управлять доступом к данным .

Действия:

Создать новую роль (пользователя) PostgreSQL с именем data_engineer_trainee (стажер) и простым паролем.
Предоставить data_engineer_trainee право SELECT на таблицу Sales.
Тест 1: 

(В новой сессии) подключитесь как data_engineer_trainee и выполните SELECT * FROM Sales;.
Как data_engineer_trainee, попытаться выполнить INSERT новой продажи в Sales. (Должно завершиться неудачей).
Как пользователь-администратор, предоставить data_engineer_trainee права INSERT и UPDATE на таблицу Sales.
Тест 2: 

Как data_engineer_trainee, попробовать выполнить INSERT и UPDATE. (Теперь должно сработать).*/

CREATE USER data_engineer_trainee WITH PASSWORD 'trainee123';
GRANT SELECT ON TABLE sales TO data_engineer_trainee;

GRANT INSERT, UPDATE ON TABLE sales TO data_engineer_trainee;

-- Подключаемся с нового data_engineer_trainee

SELECT * FROM Sales;--сработало
INSERT INTO sales (sales_id, total_price) VALUES (9999999, 100.0); -- не сработало

INSERT INTO sales (sales_id, employee_id, customer_id, product_id, quantity, total_price, transaction_number) 
VALUES (7000001, 1, 1, 1, 1, 100.0, 'T_TEST_1');-- сработало

UPDATE sales SET total_price = 150.0 WHERE sales_id = 7000001; -- сработало

/*Задание 4: DML/DCL (Сложные операции с пайплайнами)
Цель: Практика DML с использованием WHERE, JOIN и транзакций для поддержки Data Platform.

Действия:

Увеличить цену всех продуктов категории 'Dairy' на 10%.
Удалить всех сотрудников без продаж.
Вставить нового сотрудника и первую продажу в одной транзакции.*/

-- 1. Увеличить цену всех продуктов категории 'Dairy' на 10%
-- Используем подзапрос, чтобы найти ID категории по её имени
UPDATE products
SET price = price * 1.10
WHERE category_id = (
    SELECT category_id 
    FROM categories 
    WHERE category_name = 'Dairy'
);

-- 2. Удалить всех сотрудников без продаж
-- Используем оператор NOT IN или NOT EXISTS
DELETE FROM employees
WHERE employee_id NOT IN (
    SELECT DISTINCT employee_id 
    FROM sales 
    WHERE employee_id IS NOT NULL
);

-- 3. Вставить нового сотрудника и первую продажу в одной транзакции
BEGIN; -- Начало транзакции

-- Добавляем нового сотрудника (ID 24, так как их было 23)
INSERT INTO employees (employee_id, first_name, last_name, shop_id, hire_date)
VALUES (24, 'Ivan', 'Ivanov', 1, '2023-10-27');

-- Добавляем его первую продажу
-- Важно: используем тот же employee_id (24)
INSERT INTO sales (sales_id, employee_id, product_id, quantity, total_price, transaction_number)
VALUES (7000005, 24, 1, 5, 500.00, 'T_NEW_EMP_001');
commit;

/*Задание 5: Функции и Представления (Views для Gold Layer)
Цель: Создать SQL-функции для расчета KPI и "витрины" (Views) для Gold-слоя, к которым будут подключаться аналитики.

Действия:

Функция: Создать функцию AvgSalesPerEmployee (PL/pgSQL), для вычисления средней суммы продаж для сотрудника.
Представление (View): Создать представление FullStatShops для суммарной статистики по магазинам с колонками (shop_id, shop_address, country, total_sales_count, total_sales_amount).*/
CREATE OR REPLACE FUNCTION AvgSalesPerEmployee(emp_id INT)
RETURNS NUMERIC AS $$
DECLARE
    avg_val NUMERIC;
BEGIN
    SELECT AVG(total_price) INTO avg_val
    FROM sales
    WHERE employee_id = emp_id;
    
    RETURN COALESCE(avg_val, 0); -- Если продаж нет, вернем 0 вместо NULL
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE VIEW FullStatShops AS
SELECT 
    sh.shop_id, 
    sh.shop_address, -- Используем новое имя колонки из Задания 2
    co.country_name AS country,
    COUNT(s.sales_id) AS total_sales_count,
    SUM(s.total_price) AS total_sales_amount
FROM shops sh
JOIN cities ci ON sh.city_id = ci.city_id
JOIN countries co ON ci.country_id = co.country_id
LEFT JOIN employees e ON sh.shop_id = e.shop_id
LEFT JOIN sales s ON e.employee_id = s.employee_id
GROUP BY sh.shop_id, sh.shop_address, co.country_name;


SELECT * FROM FullStatShops WHERE country = 'Poland';


/*Задание 6: DML (Управление платформой)
Цель: Объединение DML с JOIN, подзапросами и транзакциями.

Действия:

Найти сотрудников с продажами > 1000.
Обновить класс продуктов на 'A' для категорий с общей выручкой > 5000.
Установить modify_timestamp (функция NOW()) для продуктов без даты.*/
-- 1. Найти сотрудников с продажами > 1000
-- Мы ищем тех, у кого сумма ХОТЯ БЫ ОДНОЙ продажи больше 1000
SELECT DISTINCT e.first_name, e.last_name
FROM employees e
JOIN sales s ON e.employee_id = s.employee_id
WHERE s.total_price > 1000;

-- 2. Обновить класс продуктов на 'A' для категорий с общей выручкой > 5000
-- Используем подзапрос с агрегацией для поиска нужных категорий
UPDATE products
SET class = 'A'
WHERE category_id IN (
    SELECT p.category_id
    FROM products p
    JOIN sales s ON p.product_id = s.product_id
    GROUP BY p.category_id
    HAVING SUM(s.total_price) > 5000
);

-- 3. Установить modify_timestamp (функция NOW()) для продуктов без даты
-- В базе пустые даты могут быть либо NULL, либо просто пустой строкой ''
UPDATE products
SET modify_timestamp = NOW()::varchar
WHERE modify_timestamp IS NULL 
   OR modify_timestamp = '';
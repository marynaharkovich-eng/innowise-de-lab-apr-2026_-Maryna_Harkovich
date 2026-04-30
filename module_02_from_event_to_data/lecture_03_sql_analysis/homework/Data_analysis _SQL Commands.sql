-- Часть 1: JOIN (Связывание данных)
-- Задача 1: Вывести для каждой продажи название продукта, 
--его категорию и магазин (предполагается shops.address и связь идёт через employee -> shop)

SELECT 
    p.product_name, 
    c.category_name, 
    sh.address AS shop_address
FROM sales s
JOIN products p ON s.product_id = p.product_id
JOIN categories c ON p.category_id = c.category_id
JOIN employees e ON s.employee_id = e.employee_id
JOIN shops sh ON e.shop_id = sh.shop_id
LIMIT 10;

--Часть 2: WHERE (Фильтрация данных)
--Задача 1: Вывести все магазины расположенные в 'Poland'. #
--Необходимые колонки: shop_id, address, city_name, country.

SELECT 
    s.shop_id, 
    s.address, 
    ci.city_name, 
    co.country_name AS country
FROM shops s
JOIN cities ci ON s.city_id = ci.city_id
JOIN countries co ON ci.country_id = co.country_id
WHERE co.country_name = 'Poland';

--Задача 2: Вывести все транзакции с суммой продажи выше 1500 (total_price > 1500) для продуктов класса B (class = 'B'), 
--выполнить сортировку по номеру транзакции.

SELECT 
    s.* FROM sales s
JOIN products p ON s.product_id = p.product_id
WHERE s.total_price > 1500 
  AND p.class = 'B'
ORDER BY s.transaction_number;


--Часть 3: GROUP BY 
--Задача 1 : Вывести количество магазинов (Shops)
--в каждой стране и отсортировать по количеству магазинов по убыванию
SELECT 
    co.country_name, 
    COUNT(s.shop_id) AS shops_count
FROM shops s
JOIN cities ci ON s.city_id = ci.city_id
JOIN countries co ON ci.country_id = co.country_id
GROUP BY co.country_name
ORDER BY shops_count DESC;

--Часть 4: Having 
--Задача 1: Вывести по каждому продукту сумму продаж и средний чек, где сумма продаж выше 400,000.00 .
--Так же отсортируйте вывод по сумме продаж по убыванию. 
SELECT 
    p.product_name, 
    SUM(s.total_price) AS total_sales_sum, 
    AVG(s.total_price) AS average_check
FROM sales s
JOIN products p ON s.product_id = p.product_id
GROUP BY p.product_name
HAVING SUM(s.total_price) > 400000
ORDER BY total_sales_sum DESC;

--Часть 5: SUBQUERIES (Подзапросы)
--Задача 1: Вывести Имя и Фамилию продавца, который совершил продажу с максимальной суммой 
--и вывести адрес магазина, в котором он работает.
SELECT 
    e.first_name, 
    e.last_name, 
    sh.address AS shop_address
FROM employees e
JOIN shops sh ON e.shop_id = sh.shop_id
JOIN sales s ON e.employee_id = s.employee_id
WHERE s.total_price = (SELECT MAX(total_price) FROM sales);

--Часть 6: WINDOW FUNCTIONS (Оконные функции)
--Задача 1: Найти выручку всех магазинов в Германии по месяцам и разницу с предыдущим месяцем. 
--Применить сортировку по месяцам по возрастанию.
WITH monthly_revenue AS (
    SELECT 
        DATE_TRUNC('month', NULLIF(s.sales_timestamp, '')::timestamp) AS sale_month,
        SUM(s.total_price) AS current_month_revenue
    FROM sales s
    JOIN employees e ON s.employee_id = e.employee_id
    JOIN shops sh ON e.shop_id = sh.shop_id
    JOIN cities ci ON sh.city_id = ci.city_id
    JOIN countries co ON ci.country_id = co.country_id
    WHERE co.country_name = 'Germany'
      AND s.sales_timestamp IS NOT NULL 
      AND s.sales_timestamp <> ''
    GROUP BY 1
)
SELECT 
    sale_month,
    current_month_revenue,
    -- Добавляем столбец с данными за прошлый месяц
    LAG(current_month_revenue) OVER (ORDER BY sale_month) AS previous_month_revenue,
    -- Оставляем расчет разницы
    current_month_revenue - LAG(current_month_revenue) OVER (ORDER BY sale_month) AS revenue_diff
FROM monthly_revenue
ORDER BY sale_month;

/*Часть 7 : Финал
Для каждого магазина рассчитать агрегаты продаж и аналитические показатели в разрезе страны.

Для каждого магазина посчитать:

количество продаж (COUNT(sales_id))
общую сумму продаж (SUM(total_price))
Оставить только магазины, у которых не менее 2 продаж.

 

Для каждого такого магазина рассчитать:

долю оборота магазина от общего оборота страны
ранг магазина по сумме продаж внутри своей страны
накопительный оборот по стране,
отсортированный по убыванию оборота магазина
Отсортировать результат:

по стране
по рангу магазина*/

WITH shop_stats AS (
    -- ШАГ 1: Считаем базовые показатели для каждого магазина
    SELECT 
        co.country_name,
        sh.shop_id,
        sh.address,
        COUNT(s.sales_id) AS sales_count,
        SUM(s.total_price) AS shop_revenue
    FROM sales s
    JOIN employees e ON s.employee_id = e.employee_id
    JOIN shops sh ON e.shop_id = sh.shop_id
    JOIN cities ci ON sh.city_id = ci.city_id
    JOIN countries co ON ci.country_id = co.country_id
    GROUP BY co.country_name, sh.shop_id, sh.address
    -- Условие: не менее 2 продаж
    HAVING COUNT(s.sales_id) >= 2
)
-- ШАГ 2: Рассчитываем аналитические показатели внутри страны
SELECT 
    country_name,
    shop_id,
    address,
    sales_count,
    shop_revenue,
    -- 1. Доля оборота магазина от общего оборота страны
    shop_revenue / SUM(shop_revenue) OVER (PARTITION BY country_name) AS revenue_share,
    -- 2. Ранг магазина по сумме продаж внутри страны
    RANK() OVER (PARTITION BY country_name ORDER BY shop_revenue DESC) AS shop_rank,
    -- 3. Накопительный оборот по стране (Running Total)
    SUM(shop_revenue) OVER (PARTITION BY country_name ORDER BY shop_revenue DESC) AS running_total_revenue
FROM shop_stats
ORDER BY country_name, shop_rank;
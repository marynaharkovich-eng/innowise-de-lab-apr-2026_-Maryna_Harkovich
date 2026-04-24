## Описание внешних ключей (FK)

Foreign Key (FK) — это поле, которое ссылается на PK в другой таблице для установления связи.

## Таблица Sales:

* employee_id → ссылается на Employees.employee_id.

* customer_id → ссылается на Customers.customer_id.

* product_id → ссылается на Products.product_id.

* shop_id (подразумевается через логику) → ссылается на Shops.shop_id.

## Таблица Employees:

* city_id → ссылается на Cities.city_id.

* shop_id → ссылается на Shops.shop_id.

## Таблица Customers:

* city_id → ссылается на Cities.city_id.

## Таблица Cities:

* country_id → ссылается на Countries.country_id.

## Таблица Products:

* category_id → ссылается на Categories.category_id.

## Таблица Shops:

* city_id → ссылается на Cities.city_id.
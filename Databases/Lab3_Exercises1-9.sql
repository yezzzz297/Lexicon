SELECT COUNT(*) FROM orders;
-- Expected: 15


-- Exercise 1
-- Add myself as customer 11

INSERT INTO customers (customer_id, first_name, last_name, email)
VALUES (11, 'Yetnayet', 'Belachew', 'yeti@example.com');


-- Exercise 2
-- Add two new products

INSERT INTO products (name, category, price, stock)
VALUES
('Scarf', 'Accessories', 229, 15),
('Gloves', 'Accessories', 199, 20);


-- Exercise 3
-- Emma orders 2 Beanies

INSERT INTO orders (order_id, customer_id, order_date)
VALUES (16, 7, date('now'));

INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (16, 10, 2, 179);

-- Exercise 4
-- Try to add an order item with quantity 0

INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (16, 10, 0, 179);

-- Expected: CHECK constraint error
-- Quantity must be greater than 0


-- Exercise 5
-- Order 12 has been shipped

UPDATE orders
SET status = 'shipped'
WHERE order_id = 12;


-- Exercise 6
-- Water Bottle is back in stock

UPDATE products
SET stock = 50
WHERE product_id = 5;


-- Exercise 7
-- Increase the price of Accessories by 10%

UPDATE products
SET price = price * 1.10
WHERE category = 'Accessories';


-- Exercise 8
-- Delete the cancelled order
-- Delete its order items first

DELETE FROM order_items
WHERE order_id IN (
    SELECT order_id
    FROM orders
    WHERE status = 'cancelled'
);

DELETE FROM orders
WHERE status = 'cancelled';

-- Order items must be deleted first
-- because they are connected to orders
-- by a foreign key.


-- Exercise 9

SELECT COUNT(*) FROM orders;

-- Expected: 15
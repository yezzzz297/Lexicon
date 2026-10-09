SELECT COUNT(*) FROM orders;

-- Exercise 1
-- Show all orders with customer names and status

SELECT orders.order_id, customers.first_name,
       customers.last_name, orders.status
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id;

-- Exercise 2
-- Show Erik's orders

SELECT orders.*
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id
WHERE customers.first_name = 'Erik';


-- Exercise 3
-- Show orders from Göteborg, newest first

SELECT orders.*
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id
WHERE customers.city = 'Göteborg'
ORDER BY orders.order_date DESC;

-- Exercise 4
-- Show order items with product name and category

SELECT order_items.*, products.name, products.category
FROM order_items
JOIN products
ON order_items.product_id = products.product_id;


-- Exercise 5
-- Show orders that have Shoes

SELECT order_items.order_id, products.name
FROM order_items
JOIN products
ON order_items.product_id = products.product_id
WHERE products.name = 'Shoes';


-- Exercise 6
-- Show receipt for order 10

SELECT products.name, order_items.quantity,
       order_items.unit_price,
       order_items.quantity * order_items.unit_price AS line_total
FROM order_items
JOIN products
ON order_items.product_id = products.product_id
WHERE order_items.order_id = 10;


-- Exercise 7
-- Show customers who bought Hoodie Black

SELECT customers.first_name, orders.order_date
FROM customers
JOIN orders
ON customers.customer_id = orders.customer_id
JOIN order_items
ON orders.order_id = order_items.order_id
JOIN products
ON order_items.product_id = products.product_id
WHERE products.name = 'Hoodie Black';


-- Exercise 8
-- Show all customers and their orders
-- Also show customers without orders

SELECT customers.first_name, customers.last_name,
       orders.order_id
FROM customers
LEFT JOIN orders
ON customers.customer_id = orders.customer_id;

-- Exercise 9
-- Show products that have never been sold

SELECT products.name
FROM products
LEFT JOIN order_items
ON products.product_id = order_items.product_id
WHERE order_items.product_id IS NULL;


-- Exercise 10
-- Show Uppsala customers and what they bought

SELECT customers.first_name, products.name,
       order_items.quantity
FROM customers
JOIN orders
ON customers.customer_id = orders.customer_id
JOIN order_items
ON orders.order_id = order_items.order_id
JOIN products
ON order_items.product_id = products.product_id
WHERE customers.city = 'Uppsala';

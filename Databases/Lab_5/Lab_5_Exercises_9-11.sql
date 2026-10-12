-- Exercise 9: products Anna (customer 1) bought, each name once.
SELECT DISTINCT products.name
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id
JOIN order_items ON orders.order_id = order_items.order_id
JOIN products ON order_items.product_id = products.product_id
WHERE customers.customer_id = 1;

-- Exercise 10: correct Erik Johansson's email.
UPDATE customers
SET email = 'erik.johansson@example.com'
WHERE first_name = 'Erik' AND last_name = 'Johansson';

SELECT first_name, last_name, email
FROM customers
WHERE first_name = 'Erik' AND last_name = 'Johansson';


-- Exercise 11: show useful support information without email.
-- LEFT JOIN includes customers who have no orders.
-- COUNT(order_id) gives 0 for those customers.
CREATE VIEW customer_overview AS
SELECT customers.customer_id, customers.first_name, customers.city,
       COUNT(orders.order_id) AS number_of_orders
FROM customers
LEFT JOIN orders ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_id, customers.first_name, customers.city;

SELECT * FROM customer_overview;

-- Exercise 12
-- I would ask why the shop needs a birth date, because
-- "just in case" is not a clear purpose.
-- I would only collect it if needed for that purpose;
-- otherwise, I would leave the column out.
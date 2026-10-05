-- LEVEL 1

-- Exercise 1

SELECT *
FROM products
WHERE category != 'Accessories'
  AND stock > 0
  AND name LIKE '% %'
ORDER BY category ASC, price DESC;


-- Exercise 2

SELECT *
FROM customers
WHERE city LIKE 'S%'
   OR city LIKE 'M%'
   OR city IS NULL;


-- Exercise 3

SELECT *
FROM products
WHERE category = 'Shoes'
ORDER BY price DESC
LIMIT 1 OFFSET 1;


-- Exercise 4

SELECT *
FROM customers
WHERE joined_date > '2023-12-31'
  AND joined_date < '2026-01-01'
ORDER BY joined_date DESC
LIMIT 3;

-- LEVEL 2

-- Exercise 5

SELECT first_name || ' ' || last_name AS full_name
FROM customers
ORDER BY last_name;


-- Exercise 6

SELECT name, price,
       CASE
           WHEN price < 200 THEN 'budget'
           WHEN price < 800 THEN 'mid'
           ELSE 'premium'
       END AS price_level
FROM products;


-- Exercise 7

SELECT first_name,
       COALESCE(city, 'Unknown') AS city
FROM customers;


-- Exercise 8

SELECT *
FROM customers
WHERE CAST(strftime('%m', joined_date) AS INTEGER)
      BETWEEN 1 AND 6;


-- Exercise 9

SELECT *
FROM products
ORDER BY LENGTH(name) DESC
LIMIT 1;


-- Exercise 10

SELECT email,
       substr(email, 1, instr(email, '@') - 1) AS email_username
FROM customers;


-- LEVEL 3

-- Exercise 11

SELECT *
FROM products
WHERE price > (
    SELECT AVG(price)
    FROM products
);

-- Exercise 12

SELECT name || ' costs ' ||
       CAST(price AS INTEGER) ||
       ' kr' AS price_list
FROM products
WHERE stock > 0
ORDER BY price ASC;

-- Exercise 13

SELECT city, COUNT(*) AS customer_count
FROM customers
GROUP BY city
ORDER BY customer_count DESC;
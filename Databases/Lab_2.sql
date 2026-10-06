-- Exercise 1
CREATE TABLE books (
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT,
    year INTEGER
);

-- Exercise 2
DROP TABLE books;

CREATE TABLE books (
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT,
    year INTEGER CHECK (year > 1400)
);


-- Exercise 3
ALTER TABLE books
ADD COLUMN isbn TEXT;


-- Exercise 4
DROP TABLE books;


-- Exercise 5
PRAGMA foreign_keys = ON;

CREATE TABLE reviews (
    review_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    rating INTEGER CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Exercise 6
-- This should FAIL because rating 6 is not allowed.
INSERT INTO reviews (review_id, product_id, rating, comment)
VALUES (1, 1, 6, 'Great product');


-- Exercise 7
-- This should FAIL if product_id 50 does not exist.
INSERT INTO reviews (review_id, product_id, rating, comment)
VALUES (2, 50, 4, 'Good product');

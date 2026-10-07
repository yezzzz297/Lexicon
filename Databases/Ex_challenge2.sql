-- Exercise 1

CREATE TABLE suppliers (
    supplier_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    country TEXT DEFAULT 'Sweden',
    email TEXT
);


-- Exercise 2

INSERT INTO suppliers (supplier_id, name, email)
VALUES (1, 'Nordic Textiles', 'info@nordic.com');

SELECT * FROM suppliers;

-- Country becomes Sweden


-- Exercise 3

INSERT INTO suppliers (supplier_id, name, email)
VALUES (2, 'Nordic Textiles', 'nordic@test.com');

-- Gives an error because the name must be unique


-- Exercise 4

CREATE TABLE coupons (
    code TEXT PRIMARY KEY,
    discount_percent INTEGER CHECK (discount_percent BETWEEN 1 AND 90),
    valid_until TEXT NOT NULL
);

INSERT INTO coupons
VALUES ('SUMMER20', 95, '2026-12-31');

-- Gives an error because 95 is more than 90


-- Exercise 5

INSERT INTO suppliers (name, email)
VALUES ('Swedish Fabrics', 'info@swedish.com');

SELECT * FROM suppliers;

-- supplier_id is added automatically


-- Exercise 6

ALTER TABLE suppliers
RENAME COLUMN email TO contact_email;


-- Exercise 7

PRAGMA table_info(products);


-- Exercise 8

CREATE TABLE product_suppliers (
    product_id INTEGER,
    supplier_id INTEGER,
    purchase_price REAL CHECK (purchase_price > 0),

    PRIMARY KEY (product_id, supplier_id),

    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

INSERT INTO product_suppliers
VALUES (1, 99, 100);

-- Gives an error because supplier 99 does not exist


-- Exercise 9

CREATE TABLE campaigns (
    name TEXT,
    start_date TEXT,
    end_date TEXT,
    CHECK (end_date >= start_date)
);

INSERT INTO campaigns
VALUES ('Summer Sale', '2026-07-01', '2026-06-01');

-- Gives an error because end_date is before start_date


-- Exercise 10

CREATE TABLE product_sizes (
    id INTEGER PRIMARY KEY,
    product_id INTEGER,
    size TEXT CHECK (size IN ('S', 'M', 'L', 'XL')),
    stock INTEGER DEFAULT 0,

    UNIQUE (product_id, size),

    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO product_sizes (product_id, size)
VALUES (1, 'M');

INSERT INTO product_sizes (product_id, size)
VALUES (1, 'M');

-- First one works
-- Second one gives an error


-- Exercise 11

CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    name TEXT,
    manager_id INTEGER,

    FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
);

INSERT INTO employees
VALUES (1, 'Boss', NULL);

INSERT INTO employees
VALUES (2, 'Anna', 1);

INSERT INTO employees
VALUES (3, 'Erik', 1);

SELECT * FROM employees;

-- Should show 3 employees


-- Exercise 12

CREATE TABLE teams (
    team_id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE players (
    player_id INTEGER PRIMARY KEY,
    name TEXT,
    team_id INTEGER,

    FOREIGN KEY (team_id) REFERENCES teams(team_id)
    ON DELETE CASCADE
);

INSERT INTO teams
VALUES (1, 'Team A');

INSERT INTO players
VALUES (1, 'Anna', 1);

INSERT INTO players
VALUES (2, 'Erik', 1);

DELETE FROM teams
WHERE team_id = 1;

SELECT * FROM players;

-- Should show 0 players
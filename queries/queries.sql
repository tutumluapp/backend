--- Query for returning all the prices for a product in ascending order

SELECT p.name, pr.price
FROM products p
JOIN prices pr ON p.gtin = pr.product_id
WHERE p.gtin = 8690504063476
ORDER BY pr.price ASC;

--- Query for returning the lowest price product
SELECT p.name, pr.price
FROM products p
JOIN prices pr ON p.gtin = pr.product_id
WHERE p.gtin = 8690504063476
ORDER BY pr.price ASC
LIMIT 1;

--- Query for inserting a new price from a scanned slip
INSERT INTO prices (price, product_id)
SELECT NEW_PRICE, p.gtin
FROM products p
WHERE p.name = PRODUCT_NAME_FROM_THE_SLIP_SCAN;

--- Query for inserting with GTIN number
INSERT INTO prices (price, product_id)
SELECT NEW_PRICE, GTIN;
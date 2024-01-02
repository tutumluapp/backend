---Query for returning all the prices for a product in ascending order

SELECT p.name, pr.price
FROM products p
JOIN prices pr ON p.gtin = pr.product_id
WHERE p.gtin = 8690504063476
ORDER BY pr.price ASC

--- Query for returning the lowest price product
SELECT p.name, pr.price
FROM products p
JOIN prices pr ON p.gtin = pr.product_id
WHERE p.gtin = 8690504063476
ORDER BY pr.price ASC
LIMIT 1
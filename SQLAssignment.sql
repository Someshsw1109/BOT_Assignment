-- Start a transaction
BEGIN;

-- Create a temporary table to store old prices
CREATE TEMPORARY TABLE old_prices AS
SELECT id, price AS old_price
FROM products;

-- Update the prices in the products table
UPDATE products
SET price = price * 1.1;

-- Select and display the results
SELECT 
    p.id,
    p.name,
    op.old_price,
    p.price AS new_price,
    (p.price - op.old_price) AS price_increase
FROM 
    products p
JOIN 
    old_prices op ON p.id = op.id
ORDER BY 
    p.id;

-- Drop the temporary table
DROP TABLE old_prices;

-- Commit the transaction
COMMIT;
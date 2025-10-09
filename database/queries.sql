-- Common SQL Queries for Demo

-- 1. Get all active customers with their total spending
SELECT 
    c.customer_id,
    c.first_name || ' ' || c.last_name as full_name,
    c.email,
    COUNT(o.order_id) as order_count,
    COALESCE(SUM(o.total_amount), 0) as total_spent
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE c.status = 'active'
GROUP BY c.customer_id, c.first_name, c.last_name, c.email
ORDER BY total_spent DESC;

-- 2. Get top selling products
SELECT 
    p.product_name,
    p.category,
    SUM(oi.quantity) as units_sold,
    SUM(oi.subtotal) as total_revenue
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name, p.category
ORDER BY total_revenue DESC
LIMIT 10;

-- 3. Get orders with customer and product details
SELECT 
    o.order_id,
    c.first_name || ' ' || c.last_name as customer_name,
    o.order_date,
    o.status,
    p.product_name,
    oi.quantity,
    oi.unit_price,
    oi.subtotal
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
ORDER BY o.order_date DESC;

-- 4. Find products with low stock (less than 50 units)
SELECT 
    product_name,
    category,
    stock_quantity,
    price
FROM products
WHERE stock_quantity < 50
ORDER BY stock_quantity ASC;

-- 5. Calculate monthly sales revenue
SELECT 
    strftime('%Y-%m', order_date) as month,
    COUNT(order_id) as order_count,
    SUM(total_amount) as monthly_revenue
FROM orders
WHERE status != 'cancelled'
GROUP BY strftime('%Y-%m', order_date)
ORDER BY month DESC;

-- 6. Get customers who haven't ordered in the last 30 days
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    c.email,
    MAX(o.order_date) as last_order_date
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE c.status = 'active'
GROUP BY c.customer_id, c.first_name, c.last_name, c.email
HAVING last_order_date IS NULL OR last_order_date < date('now', '-30 days')
ORDER BY last_order_date;

-- 7. Get average order value by customer
SELECT 
    c.customer_id,
    c.first_name || ' ' || c.last_name as customer_name,
    COUNT(o.order_id) as total_orders,
    AVG(o.total_amount) as avg_order_value,
    SUM(o.total_amount) as total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, customer_name
HAVING COUNT(o.order_id) > 0
ORDER BY avg_order_value DESC;

-- 8. Get product categories with their performance
SELECT 
    p.category,
    COUNT(DISTINCT p.product_id) as product_count,
    SUM(oi.quantity) as total_units_sold,
    SUM(oi.subtotal) as total_revenue,
    AVG(p.price) as avg_product_price
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;

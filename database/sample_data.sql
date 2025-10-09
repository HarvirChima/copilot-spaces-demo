-- Sample data for customers table
INSERT INTO customers (first_name, last_name, email, phone, address, city, state, zip_code) VALUES
('John', 'Doe', 'john.doe@example.com', '555-0100', '123 Main St', 'Seattle', 'WA', '98101'),
('Jane', 'Smith', 'jane.smith@example.com', '555-0101', '456 Oak Ave', 'Portland', 'OR', '97201'),
('Bob', 'Johnson', 'bob.johnson@example.com', '555-0102', '789 Pine Rd', 'San Francisco', 'CA', '94102'),
('Alice', 'Brown', 'alice.brown@example.com', '555-0103', '321 Elm St', 'Austin', 'TX', '78701'),
('Charlie', 'Wilson', 'charlie.wilson@example.com', '555-0104', '654 Maple Dr', 'Denver', 'CO', '80201');

-- Sample data for products table
INSERT INTO products (product_name, description, category, price, stock_quantity, sku) VALUES
('Laptop Pro 15', 'High-performance laptop with 15-inch display', 'Electronics', 1299.99, 45, 'LAP-PRO-15'),
('Wireless Mouse', 'Ergonomic wireless mouse with USB receiver', 'Electronics', 29.99, 150, 'MOU-WIR-01'),
('Office Chair Deluxe', 'Ergonomic office chair with lumbar support', 'Furniture', 349.99, 30, 'CHR-OFF-DLX'),
('Standing Desk', 'Adjustable height standing desk', 'Furniture', 599.99, 20, 'DSK-STD-01'),
('USB-C Hub', '7-port USB-C hub with HDMI and ethernet', 'Electronics', 49.99, 80, 'HUB-USC-07'),
('Noise Cancelling Headphones', 'Premium over-ear headphones', 'Electronics', 199.99, 60, 'HDP-NC-01'),
('Ergonomic Keyboard', 'Split keyboard with wrist rest', 'Electronics', 89.99, 75, 'KEY-ERG-01'),
('Monitor 27inch 4K', '27-inch 4K IPS display', 'Electronics', 449.99, 35, 'MON-27-4K');

-- Sample data for orders table
INSERT INTO orders (customer_id, total_amount, status, shipping_address) VALUES
(1, 1349.98, 'delivered', '123 Main St, Seattle, WA 98101'),
(2, 679.98, 'shipped', '456 Oak Ave, Portland, OR 97201'),
(1, 89.99, 'processing', '123 Main St, Seattle, WA 98101'),
(3, 599.99, 'pending', '789 Pine Rd, San Francisco, CA 94102'),
(4, 249.98, 'delivered', '321 Elm St, Austin, TX 78701');

-- Sample data for order_items table
INSERT INTO order_items (order_id, product_id, quantity, unit_price, subtotal) VALUES
-- Order 1
(1, 1, 1, 1299.99, 1299.99),
(1, 5, 1, 49.99, 49.99),
-- Order 2
(2, 3, 1, 349.99, 349.99),
(2, 4, 1, 599.99, 599.99),
-- Order 3
(3, 7, 1, 89.99, 89.99),
-- Order 4
(4, 4, 1, 599.99, 599.99),
-- Order 5
(5, 2, 2, 29.99, 59.98),
(5, 6, 1, 199.99, 199.99);

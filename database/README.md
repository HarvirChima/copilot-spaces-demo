# Database Schema

SQL database schema for a customer order management system.

## Files

- `schema.sql` - Complete database schema with tables, indexes, and views
- `sample_data.sql` - Sample data to populate the database
- `queries.sql` - Common SQL queries for data analysis

## Database Structure

### Tables

1. **customers** - Customer information
   - customer_id (PK)
   - first_name, last_name, email, phone
   - address, city, state, zip_code
   - status, created_at, updated_at

2. **products** - Product catalog
   - product_id (PK)
   - product_name, description, category
   - price, stock_quantity, sku
   - created_at, updated_at

3. **orders** - Customer orders
   - order_id (PK)
   - customer_id (FK)
   - order_date, total_amount, status
   - shipping_address, tracking_number

4. **order_items** - Order line items
   - order_item_id (PK)
   - order_id (FK), product_id (FK)
   - quantity, unit_price, subtotal

### Views

- `customer_order_summary` - Aggregated customer order statistics
- `product_sales_summary` - Product sales performance metrics

## Setup

### SQLite
```bash
sqlite3 store.db < schema.sql
sqlite3 store.db < sample_data.sql
```

### PostgreSQL
```bash
psql -d your_database < schema.sql
psql -d your_database < sample_data.sql
```

### MySQL
```bash
mysql -u username -p database_name < schema.sql
mysql -u username -p database_name < sample_data.sql
```

## Demo Ideas for Copilot Spaces

1. **Add New Tables**: "Create a reviews table to store product reviews with ratings"
2. **Complex Query**: "Write a query to find customers who ordered products in multiple categories"
3. **Add Triggers**: "Create triggers to automatically update the updated_at timestamp"
4. **Add Stored Procedures**: "Create a stored procedure to process a new order"
5. **Migration Script**: "Write a migration to add a loyalty points system"
6. **Performance Optimization**: "Analyze and optimize slow queries with proper indexes"
7. **Add Constraints**: "Add check constraints to ensure data integrity"

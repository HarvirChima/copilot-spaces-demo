"""
Product Inventory Analysis Script
Processes CSV product data and generates inventory insights
"""

import csv
from collections import defaultdict

def load_product_data(filename='products.csv'):
    """Load product data from CSV file"""
    products = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['price'] = float(row['price'])
            row['stock_quantity'] = int(row['stock_quantity'])
            products.append(row)
    return products

def analyze_by_category(products):
    """Analyze products by category"""
    category_data = defaultdict(lambda: {
        'count': 0,
        'total_value': 0,
        'total_stock': 0,
        'products': []
    })
    
    for product in products:
        cat = product['category']
        value = product['price'] * product['stock_quantity']
        
        category_data[cat]['count'] += 1
        category_data[cat]['total_value'] += value
        category_data[cat]['total_stock'] += product['stock_quantity']
        category_data[cat]['products'].append(product['product_name'])
    
    return dict(category_data)

def find_low_stock_items(products, threshold=50):
    """Find products with stock below threshold"""
    return [p for p in products if p['stock_quantity'] < threshold]

def find_high_value_items(products, n=5):
    """Find top N highest value items"""
    for product in products:
        product['total_value'] = product['price'] * product['stock_quantity']
    
    sorted_products = sorted(products, key=lambda x: x['total_value'], reverse=True)
    return sorted_products[:n]

def generate_inventory_report(products):
    """Generate comprehensive inventory report"""
    print("="*70)
    print("PRODUCT INVENTORY ANALYSIS REPORT")
    print("="*70)
    print(f"\nTotal Products: {len(products)}")
    
    # Category Analysis
    print("\n--- Category Breakdown ---")
    category_data = analyze_by_category(products)
    for category, data in category_data.items():
        print(f"\n{category}:")
        print(f"  Product Count: {data['count']}")
        print(f"  Total Stock: {data['total_stock']} units")
        print(f"  Total Inventory Value: ${data['total_value']:,.2f}")
    
    # Low Stock Alert
    print("\n--- Low Stock Alert (< 50 units) ---")
    low_stock = find_low_stock_items(products)
    if low_stock:
        for product in low_stock:
            print(f"  {product['product_name']}: {product['stock_quantity']} units")
    else:
        print("  No low stock items")
    
    # High Value Items
    print("\n--- Top 5 High Value Inventory Items ---")
    high_value = find_high_value_items(products)
    for i, product in enumerate(high_value, 1):
        print(f"{i}. {product['product_name']}: ${product['total_value']:,.2f}")
        print(f"   (${product['price']:.2f} x {product['stock_quantity']} units)")
    
    # Overall Statistics
    total_inventory_value = sum(p['price'] * p['stock_quantity'] for p in products)
    total_stock = sum(p['stock_quantity'] for p in products)
    avg_price = sum(p['price'] for p in products) / len(products)
    
    print("\n--- Overall Statistics ---")
    print(f"Total Inventory Value: ${total_inventory_value:,.2f}")
    print(f"Total Stock Units: {total_stock}")
    print(f"Average Product Price: ${avg_price:.2f}")
    
    print("\n" + "="*70)

if __name__ == '__main__':
    products = load_product_data()
    generate_inventory_report(products)

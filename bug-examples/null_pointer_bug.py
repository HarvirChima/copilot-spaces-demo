"""
Bug Example 1: Null Pointer / None Type Error
This code has a bug that causes a TypeError when trying to access dictionary values
"""

def calculate_user_discount(user_data):
    """
    Calculate discount based on user's purchase history
    Bug: Doesn't handle None or missing keys properly
    """
    # This will fail if user_data is None or doesn't have 'purchases' key
    total_purchases = user_data['purchases']
    
    if total_purchases > 100:
        discount = 0.20
    elif total_purchases > 50:
        discount = 0.10
    else:
        discount = 0.05
    
    # This will also fail if 'email' key is missing
    email = user_data['email']
    
    return {
        'email': email,
        'discount': discount,
        'total_purchases': total_purchases
    }

def process_orders(orders):
    """
    Process a list of orders
    Bug: Doesn't handle empty or None input
    """
    total = 0
    for order in orders:
        total += order['amount']
    
    return total

# Test cases that will cause errors
if __name__ == '__main__':
    # This will cause a TypeError
    user1 = None
    result1 = calculate_user_discount(user1)
    
    # This will also cause a KeyError
    user2 = {'name': 'John'}  # Missing 'purchases' and 'email'
    result2 = calculate_user_discount(user2)
    
    # This will cause a TypeError
    orders = None
    total = process_orders(orders)
    
    print("Results:", result1, result2, total)

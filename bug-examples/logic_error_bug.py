"""
Bug Example 3: Logic Error in Calculations
This code has logical errors that produce incorrect results
"""

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers
    Bug: Incorrect calculation logic
    """
    total = 0
    count = 0
    
    for num in numbers:
        total += num
        count += 1
    
    # Bug: Doesn't handle empty list (division by zero)
    average = total / count
    return average

def apply_tax(price, tax_rate):
    """
    Apply tax to a price
    Bug: Incorrect tax calculation
    """
    # Bug: This calculates the tax amount, not the final price
    tax = price * tax_rate
    return tax  # Should return price + tax

def calculate_discount_price(original_price, discount_percent):
    """
    Calculate price after discount
    Bug: Incorrect discount logic
    """
    # Bug: This removes the discount amount twice
    discount = original_price * (discount_percent / 100)
    discounted_price = original_price - discount - discount
    return discounted_price

def is_even_number(number):
    """
    Check if a number is even
    Bug: Incorrect logic
    """
    # Bug: This logic is backwards
    if number % 2 == 1:
        return True
    else:
        return False

def get_percentage(part, whole):
    """
    Calculate what percentage 'part' is of 'whole'
    Bug: Formula is incorrect
    """
    # Bug: Formula should be (part / whole) * 100
    percentage = (whole / part) * 100
    return percentage

# Test cases
if __name__ == '__main__':
    # Test 1: Empty list causes division by zero
    empty_list = []
    avg = calculate_average(empty_list)
    print(f"Average: {avg}")
    
    # Test 2: Wrong tax calculation
    price = 100
    tax_rate = 0.08  # 8% tax
    final_price = apply_tax(price, tax_rate)
    print(f"Price with tax: ${final_price}")  # Should be $108, but returns $8
    
    # Test 3: Wrong discount calculation
    original = 100
    discount = 20  # 20% off
    final = calculate_discount_price(original, discount)
    print(f"Discounted price: ${final}")  # Should be $80, but returns $60
    
    # Test 4: Wrong even/odd logic
    print(f"Is 4 even? {is_even_number(4)}")  # Should be True, but returns False
    print(f"Is 5 even? {is_even_number(5)}")  # Should be False, but returns True
    
    # Test 5: Wrong percentage calculation
    pct = get_percentage(25, 100)
    print(f"25 is what % of 100? {pct}")  # Should be 25%, but returns 400%

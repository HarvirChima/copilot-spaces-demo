"""
Bug Example 2: Off-by-One Error
This code has classic off-by-one errors in array/list indexing
"""

def get_first_and_last_items(items):
    """
    Get the first and last items from a list
    Bug: Incorrect indexing causes issues with edge cases
    """
    if len(items) < 1:
        return None
    
    # Bug: What if the list has only one item?
    first = items[0]
    last = items[len(items)]  # Bug: Should be len(items) - 1
    
    return first, last

def process_sublist(data, start_idx, end_idx):
    """
    Process a sublist from start to end index
    Bug: Incorrect range causes missing or extra elements
    """
    result = []
    
    # Bug: Should this be range(start_idx, end_idx) or range(start_idx, end_idx + 1)?
    for i in range(start_idx, end_idx):
        result.append(data[i])
    
    return result

def find_pairs(numbers):
    """
    Find all adjacent pairs in a list
    Bug: Incorrect loop bounds
    """
    pairs = []
    
    # Bug: This will cause an index error on the last iteration
    for i in range(len(numbers)):
        pair = (numbers[i], numbers[i + 1])
        pairs.append(pair)
    
    return pairs

# Test cases
if __name__ == '__main__':
    # Test 1: Will cause IndexError
    items = [1, 2, 3, 4, 5]
    first, last = get_first_and_last_items(items)
    print(f"First: {first}, Last: {last}")
    
    # Test 2: Edge case with single item
    single_item = [42]
    first, last = get_first_and_last_items(single_item)
    print(f"Single item - First: {first}, Last: {last}")
    
    # Test 3: Will cause IndexError
    numbers = [10, 20, 30, 40, 50]
    pairs = find_pairs(numbers)
    print(f"Pairs: {pairs}")

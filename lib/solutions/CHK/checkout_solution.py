# noinspection PyUnusedLocal
def checkout(skus: str) -> int:
    # Define the prices of items
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40
    }
    
    # Define the special offers
    offers = {
        'A': [(5, 200), (3, 130)],  # 5 A's for 200, 3 A's for 130
        'B': (2, 45),               # 2 B's for 45
    }
    
    # Count the frequency of each item in the input
    item_counts = {}
    
    # Check for invalid input (non-alphabet characters or wrong SKUs)
    for item in skus:
        if item not in prices:
            return -1  # Invalid input
        item_counts[item] = item_counts.get(item, 0) + 1
    
    # Special case for E - Buy 2 E's, get 1 B free
    if 'E' in item_counts and 'B' in item_counts:
        free_b_count = item_counts['E'] // 2  # Each 2 E's give 1 free B
        item_counts['B'] = max(0, item_counts['B'] - free_b_count)  # Remove the free B's from count
    
    # Calculate total price
    total = 0
    for item, count in item_counts.items():
        if item == 'A':
            # Special pricing for A with multiple offers
            offer_price = 0
            if count >= 5:
                offer_price += (count // 5) * 200
                count = count % 5  # Remaining A's after applying 5A offer
            if count >= 3:
                offer_price += (count // 3) * 130
                count = count % 3  # Remaining A's after applying 3A offer
            offer_price += count * prices['A']  # Add remaining A's
            total += offer_price
        elif item == 'B' and 'B' in offers:
            # Apply the offer for B
            offer_count, offer_price = offers['B']
            offer_applies = count // offer_count
            remainder = count % offer_count
            total += offer_applies * offer_price + remainder * prices['B']
        else:
            # No special offer, just add the price for each item
            total += count * prices[item]
    
    return total

# Test cases
if __name__ == "__main__":
    # Test for valid inputs with special offers
    assert checkout("AAA") == 130, "Test case 1 failed: expected 130"
    assert checkout("AAAAA") == 200, "Test case 2 failed: expected 200"
    assert checkout("AAAAAA") == 250, "Test case 3 failed: expected 250"  # 5 A's for 200, 1 A for 50
    assert checkout("AAABBB") == 205, "Test case 4 failed: expected 205"  # 130 for 3 A's, 45 for 2 B's, 30 for 1 B
    assert checkout("ABCDE") == 155, "Test case 5 failed: expected 155"  # Regular price for all items
    assert checkout("EEB") == 80, "Test case 6 failed: expected 80"  # 2 E's for 80, 1 B free

    # Test for invalid input
    assert checkout("E1") == -1, "Test case 7 failed: expected -1"
    
    print("All tests passed!")
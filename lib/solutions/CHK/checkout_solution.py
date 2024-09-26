# noinspection PyUnusedLocal
def checkout(skus: str) -> int:
    # If the input is an empty string, return 0
    if skus == "":
        return 0

    # Define the prices of items
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15
    }
    
    # Define the special offers
    offers = {
        'A': (3, 130),  # 3 A's for 130
        'B': (2, 45)    # 2 B's for 45
    }
    
    # Count the frequency of each item in the input
    item_counts = {}
    
    # Check for invalid input (non-alphabet characters or wrong SKUs)
    for item in skus:
        if item not in prices:
            return -1  # Invalid input
        item_counts[item] = item_counts.get(item, 0) + 1
    
    # Calculate total price
    total = 0
    for item, count in item_counts.items():
        if item in offers:
            offer_count, offer_price = offers[item]
            # Calculate how many times the offer applies
            offer_applies = count // offer_count
            remainder = count % offer_count
            # Add the offer price for bundles and individual prices for remaining items
            total += offer_applies * offer_price + remainder * prices[item]
        else:
            # No special offer, just add the price for each item
            total += count * prices[item]
    
    return total

# Test cases
if __name__ == "__main__":
    # Test for valid inputs with special offers
    assert checkout("AAA") == 130, "Test case 1 failed: expected 130"
    assert checkout("AAAAA") == 230, "Test case 2 failed: expected 230"
    assert checkout("AAAAAA") == 260, "Test case 3 failed: expected 260"  # 2 bundles of 3A (130 + 130)
    
    # Test for valid inputs without special offers
    assert checkout("C") == 20, "Test case 4 failed: expected 20"
    assert checkout("D") == 15, "Test case 5 failed: expected 15"
    
    # Test for mixed inputs with and without offers
    assert checkout("AAABBB") == 205, "Test case 6 failed: expected 205"  # 130 (for 3A) + 45 (for 2B) + 30 (for 1B)
    assert checkout("ABCD") == 115, "Test case 7 failed: expected 115"
    
    # Test for invalid input
    assert checkout("E") == -1, "Test case 8 failed: expected -1"
    assert checkout("AA1BB") == -1, "Test case 9 failed: expected -1"
    
    # Test for empty string
    assert checkout("") == 0, "Test case 10 failed: expected 0"
    
    print("All tests passed!")

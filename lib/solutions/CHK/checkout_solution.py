# noinspection PyUnusedLocal
def checkout(skus: str) -> int:
    # Define the prices of items
    prices = {
        'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20, 'H': 10, 'I': 35,
        'J': 60, 'K': 80, 'L': 90, 'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50,
        'S': 30, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 90, 'Y': 10, 'Z': 50
    }

    # Define the special offers
    offers = {
        'A': [(5, 200), (3, 130)],   # 5A for 200, 3A for 130
        'B': (2, 45),                # 2B for 45
        'E': '2E1B',                 # 2E get 1 B free
        'F': (3, 20),                # 3F for 20 (buy 2, get 1 free)
        'H': [(10, 80), (5, 45)],    # 10H for 80, 5H for 45
        'K': (2, 150),               # 2K for 150
        'N': '3N1M',                 # 3N get 1 M free
        'P': (5, 200),               # 5P for 200
        'Q': (3, 80),                # 3Q for 80
        'R': '3R1Q',                 # 3R get 1 Q free
        'U': (4, 120),               # 3U get 1 U free (equivalent to 4U for 120)
        'V': [(3, 130), (2, 90)]     # 3V for 130, 2V for 90
    }

    # Count the frequency of each item in the input
    item_counts = {}
    
    # Check for invalid input (non-alphabet characters or wrong SKUs)
    for item in skus:
        if item not in prices:
            return -1  # Invalid input
        item_counts[item] = item_counts.get(item, 0) + 1

    # Special case offers that involve giving a free item
    if 'E' in item_counts and 'B' in item_counts:
        free_b_count = item_counts['E'] // 2  # Each 2 E's give 1 free B
        item_counts['B'] = max(0, item_counts['B'] - free_b_count)  # Remove free B's from the count

    if 'N' in item_counts and 'M' in item_counts:
        free_m_count = item_counts['N'] // 3  # Each 3 N's give 1 free M
        item_counts['M'] = max(0, item_counts['M'] - free_m_count)  # Remove free M's from the count

    if 'R' in item_counts and 'Q' in item_counts:
        free_q_count = item_counts['R'] // 3  # Each 3 R's give 1 free Q
        item_counts['Q'] = max(0, item_counts['Q'] - free_q_count)  # Remove free Q's from the count

    if 'U' in item_counts:
        free_u_count = item_counts['U'] // 4  # Every 4 U's give 1 free U
        item_counts['U'] = max(0, item_counts['U'] - free_u_count)

    # Calculate total price
    total = 0
    for item, count in item_counts.items():
        if item in offers:
            if isinstance(offers[item], tuple):
                # Special offer with pricing (e.g., 2B for 45)
                offer_count, offer_price = offers[item]
                offer_applies = count // offer_count
                remainder = count % offer_count
                total += offer_applies * offer_price + remainder * prices[item]
            elif isinstance(offers[item], list):
                # Special offers with multiple levels (e.g., 3A for 130, 5A for 200)
                offer_price = 0
                for offer_count, offer_price_per in offers[item]:
                    offer_applies = count // offer_count
                    offer_price += offer_applies * offer_price_per
                    count %= offer_count
                total += offer_price + count * prices[item]
        else:
            # No special offer, just add the price for each item
            total += count * prices[item]
    
    return total

# Test cases
if __name__ == "__main__":
    # Testing various cases with special offers and combinations
    assert checkout("AAA") == 130, "Test case 1 failed"
    assert checkout("AAAAA") == 200, "Test case 2 failed"
    assert checkout("AAAAAAAAAA") == 400, "Test case 3 failed"  # 5A for 200, 5A for 200
    assert checkout("BB") == 45, "Test case 4 failed"
    assert checkout("BBBB") == 90, "Test case 5 failed"
    assert checkout("FFFFFF") == 40, "Test case 6 failed"  # 6F for 40 (2 free F's)
    assert checkout("EEB") == 80, "Test case 7 failed"  # 2E's for 80, 1 B free
    assert checkout("HHHHHHHHHH") == 80, "Test case 8 failed"  # 10H for 80
    assert checkout("KK") == 150, "Test case 9 failed"  # 2K for 150
    assert checkout("NNNM") == 120, "Test case 10 failed"  # 3N's for 120, 1 M free
    assert checkout("PPPPP") == 200, "Test case 11 failed"  # 5P for 200
    assert checkout("QQQ") == 80, "Test case 12 failed"  # 3Q for 80
    assert checkout("RRRQQQ") == 210, "Test case 13 failed"  # 3R for 150 + 1 Q free

    print("All tests passed!")

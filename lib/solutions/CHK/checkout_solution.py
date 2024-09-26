# noinspection PyUnusedLocal
def checkout(skus: str) -> int:
    # Define the prices of items
    prices = {
        'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20, 'H': 10, 'I': 35,
        'J': 60, 'K': 70, 'L': 90, 'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50,
        'S': 20, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 17, 'Y': 20, 'Z': 21
    }

    # Define the special offers
    offers = {
        'A': [(5, 200), (3, 130)],   # 5A for 200, 3A for 130
        'B': (2, 45),                # 2B for 45
        'F': (3, 20),                # 3F for 20 (buy 2, get 1 free)
        'H': [(10, 80), (5, 45)],    # 10H for 80, 5H for 45
        'K': (2, 120),               # 2K for 120
        'P': (5, 200),               # 5P for 200
        'Q': (3, 80),                # 3Q for 80
        'V': [(3, 130), (2, 90)]     # 3V for 130, 2V for 90
    }

    # Group discount items (S, T, X, Y, Z)
    group_discount_items = {'S', 'T', 'X', 'Y', 'Z'}

    # Count the frequency of each item in the input
    item_counts = {}

    # Check for invalid input (non-alphabet characters or wrong SKUs)
    for item in skus:
        if item not in prices:
            return -1  # Invalid input
        item_counts[item] = item_counts.get(item, 0) + 1

    # Handle free items due to special offers (e.g., 2E's give 1 free B)
    if 'E' in item_counts:
        free_b_count = item_counts['E'] // 2  # Each 2 E's give 1 free B
        if 'B' in item_counts:
            # Reduce the B count by the free B's
            item_counts['B'] = max(0, item_counts['B'] - free_b_count)

    if 'N' in item_counts:
        free_m_count = item_counts['N'] // 3  # Each 3 N's give 1 free M
        if 'M' in item_counts:
            item_counts['M'] = max(0, item_counts['M'] - free_m_count)
        else:
            item_counts['M'] = 0  # Ensure M is accounted for as 0 if not present

    if 'R' in item_counts:
        free_q_count = item_counts['R'] // 3  # Each 3 R's give 1 free Q
        if 'Q' in item_counts:
            item_counts['Q'] = max(0, item_counts['Q'] - free_q_count)
        else:
            item_counts['Q'] = 0  # Ensure Q is accounted for as 0 if not present

    if 'U' in item_counts:
        free_u_count = item_counts['U'] // 4  # Every 4 U's give 1 free U
        item_counts['U'] = max(0, item_counts['U'] - free_u_count)

    # Apply group discount for (S, T, X, Y, Z) - any 3 for 45
    group_discount_count = 0
    group_discount_items_list = []
    for item in group_discount_items:
        if item in item_counts:
            group_discount_count += item_counts[item]
            group_discount_items_list.extend([item] * item_counts[item])
    
    # Calculate total for the group discount
    group_discount_total = 0
    if group_discount_count >= 3:
        # Sort the group_discount_items_list by price descending to ensure we benefit the customer
        group_discount_items_list.sort(key=lambda x: prices[x], reverse=True)

        # Calculate group discounts and remaining items
        while len(group_discount_items_list) >= 3:
            group_discount_total += 45
            group_discount_items_list = group_discount_items_list[3:]

        # Add remaining items that did not form a group of 3 at their individual prices
        for item in group_discount_items_list:
            group_discount_total += prices[item]

    # Calculate total price for all other items (ignoring group discount items)
    total = group_discount_total
    for item, count in item_counts.items():
        if item in group_discount_items:
            continue  # Skip items that are part of the group discount

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
    assert checkout("KK") == 120, "Test case 9 failed"  # 2K for 120
    assert checkout("NNNM") == 120, "Test case 10 failed"  # 3N's for 120, 1 M free
    assert checkout("PPPPP") == 200, "Test case 11 failed"  # 5P for 200
    assert checkout("QQQ") == 80, "Test case 12 failed"  # 3Q for 80
    assert checkout("RRRQQQ") == 210, "Test case 13 failed"  # 3R for 150 + 1 Q free
    assert checkout("SXT") == 45, "Test case 14 failed"  # Group discount for 3 items (S, X, T)
    assert checkout("SSS") == 45, "Test case 15 failed"  # Group discount for 3 S's

    print("All tests passed!")
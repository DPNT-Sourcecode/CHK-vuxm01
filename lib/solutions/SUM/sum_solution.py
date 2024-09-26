# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x: int, y: int) -> int:
    # Implement the sum functionality here
    return x + y

# Test cases
if __name__ == "__main__":
    # Test the function with different inputs and expected outputs
    test_cases = [
        (10, 20, 30),   # Expected output: 30
        (0, 0, 0),      # Expected output: 0
        (50, 50, 100),  # Expected output: 100
        (100, 100, 200) # Expected output: 200
    ]
    
    # Iterate through the test cases and verify the results
    for x, y, expected in test_cases:
        result = compute(x, y)
        assert result == expected, f"Test failed for inputs ({x}, {y}): expected {expected}, got {result}"
    
    # If all tests pass, print success message
    print("All tests passed successfully!")
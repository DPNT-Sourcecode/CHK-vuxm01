# noinspection PyUnusedLocal
def hello(friend_name: str) -> str:
    # Ignore the input and return "Hello, World!"
    return "Hello, World!"
# Test cases
if __name__ == "__main__":
    # Test the function with a sample name
    result = hello("Alice")
    expected_result = "Hello, Alice!"
    
    # Assert if the result matches the expected output
    assert result == expected_result, f"Test failed: expected {expected_result}, got {result}"
    
    # Print success if the test passes
    print("Test passed successfully!")

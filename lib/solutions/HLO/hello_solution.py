# noinspection PyUnusedLocal
def hello(friend_name: str) -> str:
    # Check if the input should be ignored and return "Hello, World!" or personalized greeting
    if friend_name == "":
        return "Hello, World!"  # Case for round 1
    else:
        return f"Hello, {friend_name}!"  # Case for round 2 (personalized)

# Test cases
if __name__ == "__main__":
    # Test for Round 1: Ignoring the input and returning "Hello, World!"
    result_world = hello("")
    expected_result_world = "Hello, World!"
    assert result_world == expected_result_world, f"Test failed: expected {expected_result_world}, got {result_world}"

    # Test for Round 2: Personalized greeting
    result_personalized = hello("Alice")
    expected_result_personalized = "Hello, Alice!"
    assert result_personalized == expected_result_personalized, f"Test failed: expected {expected_result_personalized}, got {result_personalized}"
    
    # If all tests pass, print success
    print("All tests passed successfully!")


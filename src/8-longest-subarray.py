def count_long_subarrays(A):
    n = len(A)
    if n == 0:
        return 0
    
    # variables
    count_max_len = 0
    max_len = 0
    current_len = 1

    for i in range(0, n):
        if A[i] > A[i-1]:
            current_len += 1
        else:
            current_len = 1

        if current_len == max_len:
            count_max_len += 1
        elif current_len > max_len:
            max_len = current_len
            count_max_len = 1

    return count_max_len

# Test cases
def test_count_long_subarrays():
    test_cases = [
        ((1, 3, 4, 2, 7, 5, 6, 9, 8), 2),  # 2 subarrays of length 3
        ((1, 2, 3, 4, 5), 1),  # Only one increasing subarray, the entire array
        ((5, 4, 3, 2, 1), 1),  # No increasing subarray, just single elements
        ((1, 2, 1, 2, 1, 2), 3),  # Three subarrays of length 3: (1, 2)
        ((1, 2, 3, 4, 5, 6), 1),  # One longest subarray: (1, 2, 3, 4, 5, 6)
        ((1, 3, 2, 4, 6, 5, 7), 1),  # One subarray of length 3: (2, 4, 6)
    ]

    for i, (input_data, expected_result) in enumerate(test_cases):
        result = count_long_subarrays(input_data)
        print(f"Test case {i + 1}: {'Passed' if result == expected_result else 'Failed'}")

# Run tests
test_count_long_subarrays()

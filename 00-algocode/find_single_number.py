
def single_number(arr,k):
    # Initialize a list to track the count of bits at each position
    bit_counts = [0] * 32

    # Count the occurrences of each bit across all numbers
    for num in arr:
        for i in range(32):
            # Check if the i-th bit of num is set
            bit_counts[i] += (num >> i) & 1

    # Rebuild the result by checking the bit counts modulo k
    result = 0
    for i in range(32):
        # Get the bit count modulo k
        if bit_counts[i] % k != 0:
            # If it's not divisible by k, it must be part of the unique number
            result |= (1 << i)

    # Handle negative numbers (because we use 32 bits, the sign bit must be taken into account)
    if result >= 2**31:
        result -= 2**32

    return result

assert single_number([-2,-2,1,1,-3,1,-3,-3,-4,-2], 3) == -4
assert single_number([-2,-2,1,1,-3,1,-3,-3,2,-2], 3) == 2
assert single_number([2, 2, 3, 2], 3) == 3
assert single_number([2, 2, 3, 2, 2], 4) == 3
assert single_number([0, 1, 0, 1, 0, 1, 99, 0, 1], 4) == 99
assert single_number([99], 3) == 99
assert single_number([99], 8) == 99
assert single_number([3, 3, 3, 99, 3, 3, 3, 3, 3], 8) == 99
assert single_number([-3, -3, -3, -99, -3, -3, -3, -3], 7) == -99
assert single_number([-3, -99, -3], 2) == -99
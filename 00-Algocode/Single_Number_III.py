def single_number(nums):
    xor_of_2_nums = 0
    for num in nums:
        xor_of_2_nums ^= num

    bit = 0
    for bit in range(32):
        if xor_of_2_nums & (2**bit):
            break
    xor_where_bit_on = 0
    xor_where_bit_of = 0

    for num in nums:
        if num & (1 << bit):  # if its on (1)
            xor_where_bit_on ^= num
        else:
            xor_where_bit_of ^= num

    return [xor_where_bit_on, xor_where_bit_of]


assert single_number([1, 2, 1, 3, 2, 5]) == [3, 5] or [5, 3]

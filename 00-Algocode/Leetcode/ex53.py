# test

# arr = [1]
# 1

# arr = []
# 0

#arr = [0,0,0]
# 0

# arr = [-1,0]
# 0

# arr = [3,3,-7,2]
# [3,3] = 6

# arr = [-3,3,-2,2,5]
# 11


def biggest_sub_arr(nums):
    max_sum = float('-inf')

    sum = 0
    if ( len ( nums) == 1):
        return nums[0]
    elif ( len(nums)==0):
        return 0

    for i in range(0,len(nums)):
        sum = sum + nums[i]

        if(sum<0):
            sum = 0

        if(sum>max_sum):
            max_sum = sum

    return max_sum


assert biggest_sub_arr([]) == 0

print(biggest_sub_arr([1,2,3]))
assert biggest_sub_arr([1,2,3]) == 6


assert biggest_sub_arr([1,0,3]) == 4


assert biggest_sub_arr([1,-1,3]) == 3


assert biggest_sub_arr([3,3,-7,2,5]) == 7

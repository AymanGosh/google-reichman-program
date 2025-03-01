

def biggest_sub_arr(nums):
    sum, maxSum = 0, float('-inf')
    for i in range(len(nums)):
        sum += nums[i]
        if sum > maxSum:
            maxSum = sum
        if sum < 0:
            sum = 0
    return maxSum


print(biggest_sub_arr([5,4,-1,-1,-1,-6,77]))
assert biggest_sub_arr([5,4,-1,-1,-1]) ==  9


assert biggest_sub_arr([1,0,3]) == 4


assert biggest_sub_arr([1,-1,3]) == 3


assert biggest_sub_arr([3,3,-7,2,5]) == 7

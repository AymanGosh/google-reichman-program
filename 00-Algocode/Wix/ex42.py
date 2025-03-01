from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        curr_water = 0

        r_max = 0
        l_max = 0
        max_r = float('-inf')

        water_sp_r = 0
        water_all_r = 0

        while l_max < len(height) :
            while  r_max < len(height) and l_max < len(height) and height[r_max] <= height[l_max] :
                curr_water += height[l_max] - height[r_max]
                if max_r < height[r_max]:
                    max_r = height[r_max]

                r_max +=1

            print(l_max , r_max,curr_water,max_r)
            max_r = float('-inf')
            res += curr_water
            l_max = r_max
            curr_water = 0
        return res


##aproach2

# class Solution:
#     def trap(self, height: List[int]) -> int:
#
#         res = 0
#         for i in range(len(height)):
#
#             max1 = float('-inf')
#             max2 = max1
#
#             for j1 in range(i, len(height)):
#                 if (max1 < height[j1]):
#                     max1 = height[j1]
#
#             for j2 in range(i, -1, -1):
#                 if (max2 < height[j2] and max1 > height[j2]):
#                     max2 = height[j2]
#
#             res += max2 - height[i]
#
#         return res
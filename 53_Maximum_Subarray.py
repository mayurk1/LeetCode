"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""

from typing import List

class Solution:
    def maxSubArray(nums: List[int]) -> int:
    #def maxSubArray(self, nums: List[int]) -> int:
        newNum = maxTotal = nums[0]        

        for i in range(1, len(nums)):
            newNum = max(nums[i], nums[i] + newNum)
            maxTotal = max(newNum, maxTotal)

        return maxTotal	      

if __name__ == '__main__':
    print(Solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Constraints:
0 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""
from typing import List

class Solution:
    def removeDuplicates(nums: List[int]) -> int:
    #def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        k = 0
        i = 0
        while i < len(nums):
            if nums[i] != nums[k]:
                k += 1
                nums.insert(k, nums[i])
            i += 1
        return k+1


if __name__ == '__main__':
    #input = [1,1,2]
    input = [0,0,1,1,1,2,2,3,3,4]
    print(Solution.removeDuplicates(input))

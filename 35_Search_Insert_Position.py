"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List

class Solution:
    def searchInsert(nums: List[int], target: int) -> int:
    #def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i
            i += 1
            
        return len(nums)


if __name__ == '__main__':
    print(Solution.searchInsert([1,3,5,6], 5))

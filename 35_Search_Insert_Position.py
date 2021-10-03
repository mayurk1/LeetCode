"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List

# O(log n)
def searchInsert(nums: List[int], target: int) -> int:
#def searchInsert(self, nums: List[int], target: int) -> int:
    start = 0
    end = len(nums)

    while start < end:
        mid = (start + end) // 2
        if nums[mid] >= target:
            end = mid
        else:
            start = mid + 1
        
    return start

class Solution:
    # O(n)
    def searchInsert1(nums: List[int], target: int) -> int:
    #def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] >= target:
                return i
            i += 1
            
        return len(nums)


if __name__ == '__main__':
    print(Solution.searchInsert([1,3,5,6], 5))

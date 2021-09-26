"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Constraints:
0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""
from typing import List

class Solution:
    def removeElement(nums: List[int], val: int) -> int:
    #def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        k = 0
        i = 0
        while i < len(nums):
            if nums[i] != val:
                nums.insert(0,nums.pop(i))
                k += 1
            i += 1
            
        return k


if __name__ == '__main__':
    input = [0,1,2,2,3,0,4,2]
    #input = [3,2,2,3]
    print(Solution.removeElement(input, 2))

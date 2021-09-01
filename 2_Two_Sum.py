"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
"""
class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    
        result = []
        index_map = {}
        
        for index, x in enumerate(nums):
            difference = target - x
            if difference in index_map:
                result.append(index)
                result.append(index_map[difference])
                break
            else:
                index_map[x] = index
            
        return result


if __name__ == '__main__':
    print(Solution.twoSum([2,7,11,15], 9))


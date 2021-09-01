"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""
from typing import List

class Solution:
    def longestCommonPrefix(strs: List[str]) -> str:
    #def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        :type s: str
        :rtype: int
        """
        if len(strs) == 0:
            return '' 
        prefix = ''
        strs = sorted(strs)
        for i in strs[0]:
            if strs[-1].startswith(prefix + i):
                prefix += i
            else:
                break
        return prefix


if __name__ == '__main__':
    words = ["aaa","aa","aaa"]
    #words = ["flower","flow","flight"]
    #words = ["a"]
    print(Solution.longestCommonPrefix(words))

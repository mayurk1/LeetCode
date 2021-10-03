"""
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Constraints:
1 <= s.length <= 10^4
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""

from typing import List

class Solution:
    def lengthOfLastWord(s: str) -> int:  
    #def lengthOfLastWord(self, s: str) -> int: 
        i = len(s) - 1
        lastWordLen = 0
        while i >= 0:
            if s[i] != ' ':
                lastWordLen += 1
            elif lastWordLen > 0 and s[i] == ' ':
                break
            i -= 1

        return lastWordLen


if __name__ == '__main__':
    print(Solution.lengthOfLastWord("a"))

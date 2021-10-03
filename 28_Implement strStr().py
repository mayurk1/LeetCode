"""
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Constraints:
0 <= haystack.length, needle.length <= 5 * 10^4
haystack and needle consist of only lower-case English characters.
"""

class Solution:
    def strStr(haystack: str, needle: str) -> int:
    #def strStr(self, haystack: str, needle: str) -> int:   
        if needle == "":
            return 0
        i = 0
        while i < (len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                if haystack[i:(i + len(needle))] == needle:
                    return i
            i += 1

        return -1


if __name__ == '__main__':
    print(Solution.strStr("hello", "ll"))

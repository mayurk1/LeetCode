"""
Given a roman numeral, convert it to an integer.

Constraints:
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""
class Solution(object):
    def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """

        romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sum = 0
        lastValue = 0

        for x in s[::-1]:
            if romans[x] < lastValue:
                sum -= romans[x]
            else:
                sum += romans[x]
            lastValue = romans[x]
            
        return sum    


if __name__ == '__main__':
    print(Solution.romanToInt('XIV'))

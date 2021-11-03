"""
Given two binary strings a and b, return their sum as a binary string.

Constraints:
1 <= a.length, b.length <= 10^4
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""

class Solution:
    def addBinary(a: str, b: str) -> str:
    #def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result += str(carry %2)
            carry = carry // 2

        return result[::-1]

if __name__ == '__main__':
    print(Solution.addBinary('11', '1'))

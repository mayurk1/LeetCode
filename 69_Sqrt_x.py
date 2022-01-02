"""
Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

Constraints:
0 <= x <= 2^31 - 1
"""

class Solution:
    def mySqrt(x: int) -> int:
    #def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        start = 1
        end = x
        
        while start <= end:
            mid = start + (end-start) // 2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                end = mid - 1
            else:
                start = mid + 1
                

if __name__ == '__main__':
    print(Solution.mySqrt(17))
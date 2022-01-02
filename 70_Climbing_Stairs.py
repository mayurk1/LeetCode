"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Constraints:
1 <= n <= 45
"""

class Solution:
    def climbStairs(n: int) -> int:
    #def climbStairs(self, n: int) -> int:
        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3
        
        oneBefore = 2
        twoBefore = 1 
        sumSteps = 0
        
        for num in range(2,n):
            sumSteps = oneBefore + twoBefore
            twoBefore = oneBefore
            oneBefore = sumSteps
            
        return sumSteps
                

if __name__ == '__main__':
    print(Solution.climbStairs(9))
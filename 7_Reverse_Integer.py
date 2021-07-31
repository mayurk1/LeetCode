class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        y = abs(x)
        while(y>0):
		    r=int(y%10)
		    rev = rev*10 + r
		    y=int(y/10)
        
        sign = -1 if x < 0 else 1
            
        if (x == 0):
            return 0
        elif (rev < 2**31 - 1):
            return (rev * sign)
        else:
            return 0

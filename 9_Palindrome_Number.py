"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
Constraints:

-2^31 <= x <= 2^31 - 1

Follow up: Could you solve it without converting the integer to a string?
"""

# String method
# def palindrome(x):
#     return str(x) == str(x)[::-1]


# Integer method
def palindrome(x):
    reverse = 0

    if((x % 10 == 0 or x < 0) and not x == 0):
        return False

    while(x > reverse):
        reverse = reverse * 10 + x % 10
        x = x // 10

    return x == reverse or x == reverse // 10

print(palindrome(123321))

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Constraints:
1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
"""
class Solution:
    def isValid(s: str) -> bool:
    #def isValid(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        bracketMap = { ")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for c in s:
            if c in bracketMap:
                if stack and stack[-1] == bracketMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False


if __name__ == '__main__':
    input = "()[]{}"
    print(Solution.isValid(input))

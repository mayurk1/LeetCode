"""
Given an integer, convert it to a roman numeral.

1 <= num <= 3999
"""

def intToRoman(num):
    one = 'I'
    five = 'V'
    ten = 'X'
    fifty = 'L'
    hundred = 'C'
    fiveHundred = 'D'
    thousand = 'M'
    M = D = C = L = X = V = I = 0

    if num > 999:
        M = num // 1000
        D = (num % 1000) // 500
        C = (num % 100) // 100
        L = (num % 50) // 50

        return M*thousand + D*fiveHundred + C*hundred + L*fifty


print(intToRoman(1550))

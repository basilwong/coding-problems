# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:
    # A -> 1
    # B -> 2
    # C -> 3
    # ...
    # Z -> 26
    # AA -> 27
    # AB -> 28
    # ...
    
class Solution:
    def titleToNumber(self, s: str) -> int:
        # Expects capital letter as string.
        def helper(ch):
            return ord(ch) - 64
        ret = 0
        for i in range(len(s)):
            ret += (26**(len(s) - i - 1)) * helper(s[i])

        return ret

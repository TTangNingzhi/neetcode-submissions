class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alnum_lower = ("".join([c for c in s if c.isalnum()])).lower()
        return s_alnum_lower[::-1] == s_alnum_lower
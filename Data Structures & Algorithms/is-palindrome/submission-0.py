class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        def is_alphanumeric(c: str) -> bool:
            return "0" <= c <= "9" or "a" <= c <= "z" or "A" <= c <= "Z"

        while left < right:
            if not is_alphanumeric(s[left]):
                left += 1
                continue
            if not is_alphanumeric(s[right]):
                right -= 1
                continue
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        
        return True
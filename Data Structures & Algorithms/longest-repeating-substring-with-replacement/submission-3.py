class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        seen = {chr(c): 0 for c in range(ord("A"), ord("Z") + 1)}
        longest = 0
        for right in range(len(s)):
            seen[s[right]] += 1
            while right - left + 1 - max(seen.values()) > k:
                seen[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest

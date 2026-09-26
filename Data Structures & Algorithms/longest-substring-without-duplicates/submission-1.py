class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        left = 0
        occurrence = defaultdict(int)
        longest = 0
        for i, c in enumerate(s):
            if c in occurrence:
                left = max(left, occurrence[c] + 1)
            occurrence[c] = i
            longest = max(i + 1 - left, longest)
        return longest
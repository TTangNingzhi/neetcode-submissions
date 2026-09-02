class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = dict()
        for c in s:
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1
        for c in t:
            if c in counts:
                counts[c] -= 1
            else:
                counts[c] = -1
        for c in counts:
            if counts[c] != 0:
                return False
        return True
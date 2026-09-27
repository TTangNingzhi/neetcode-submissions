class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1 = {chr(c): 0 for c in range(ord("a"), ord("z") + 1)}
        count2 = {chr(c): 0 for c in range(ord("a"), ord("z") + 1)}
        for c in s1:
            count1[c] += 1
        for start in range(len(s2) - len(s1) + 1):
            if start == 0:
                for c in s2[:len(s1)]:
                    count2[c] += 1
            else:
                count2[s2[start - 1]] -= 1
                count2[s2[start + len(s1) - 1]] += 1
            if tuple(count2.values()) == tuple(count1.values()):
                return True
        return False
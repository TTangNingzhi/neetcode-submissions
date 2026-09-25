class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        groups = defaultdict(list)
        for s in strs:
            # don't sort, reduce complexity
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            # list cannot be key -> tuple
            groups[tuple(count)].append(s)
        return list(groups.values())
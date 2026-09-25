class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            index = "".join(sorted(s))
            if index not in groups:
                groups[index] = [s]
            else:
                groups[index].append(s)
        return list(groups.values())
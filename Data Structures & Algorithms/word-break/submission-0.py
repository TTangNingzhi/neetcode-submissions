class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            for w in wordDict:
                if len(w) <= i and res[i - len(w)] and s[:i].endswith(w):
                    res[i] = True
                    break
        return res[len(s)]
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                top = stack.pop()
                result[top[0]] = i - top[0]
            stack.append((i, t))
        return result
            
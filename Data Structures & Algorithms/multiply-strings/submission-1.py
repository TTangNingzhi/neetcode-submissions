class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = [0] * (len(num1) + len(num2))
        for i1, c1 in enumerate(num1[::-1]):
            for i2, c2 in enumerate(num2[::-1]):
                result[len(result) - (i1 + i2) - 1] += int(c1) * int(c2)
        for i in reversed(range(len(result))):
            if i:
                result[i-1] += result[i] // 10
                result[i] = result[i] % 10
        result_str = ""
        started = False
        for i, d in enumerate(result):
            if not started and d != 0:
                started = True
            if started:
                result_str += str(d)
        if not result_str:
            result_str = "0"
        return result_str
        
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if c == ")" and stack[-1] == "(" or c == "]" and stack[-1] == "[" or c == "}" and stack[-1] == "{":
                        stack = stack[:len(stack)-1]
                    else:
                        return False
        return len(stack) == 0
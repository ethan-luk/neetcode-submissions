class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {
            "{": "}",
            "[": "]",
            "(": ")",
        }
        for c in s:
            if c in d:
                stack.append(c)
            else:
                if len(stack) == 0 or d[stack[-1]] != c:
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0

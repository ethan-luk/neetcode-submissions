class Solution:
    def checkValidString(self, s: str) -> bool:
        cache = {} # (i, open) -> can make
        def dfs(i, open):
            if open < 0:
                return False
            if i == len(s):
                return open == 0
            if (i, open) in cache:
                return cache[(i, open)]
            
            if s[i] == '(':
                cache[(i, open)] = dfs(i + 1, open + 1)
            elif s[i] == ')':
                cache[(i, open)] = dfs(i + 1, open - 1)
            else:
                cache[(i, open)] = dfs(i + 1, open + 1) or \
                                    dfs(i + 1, open - 1) or \
                                    dfs(i + 1, open)
            return cache[(i, open)]
        return dfs(0, 0)
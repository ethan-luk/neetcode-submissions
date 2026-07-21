class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = {
            "2": 'abc',
            "3": 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        comb = []
        def dfs(i):
            if i == len(digits):
                res.append(''.join(comb))
                return
            
            for c in d[digits[i]]:
                comb.append(c)
                dfs(i+1)
                comb.pop()
        
        dfs(0)
        return res
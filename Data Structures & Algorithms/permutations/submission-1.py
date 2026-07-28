class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, perm = [], []

        def dfs(i):
            if i == len(nums):
                res.append(perm.copy())
            
            for x in nums:
                if x not in perm:
                    perm.append(x)
                    dfs(i+1)
                    perm.pop()
        
        dfs(0)
        return res
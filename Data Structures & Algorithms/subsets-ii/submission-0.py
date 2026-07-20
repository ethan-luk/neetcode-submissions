class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        nums.sort()
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # include in subset
            subset.append(nums[i])
            dfs(i+1)

            # don't include in subset
            subset.pop()
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            dfs(i+1)
        
        dfs(0)
        return res
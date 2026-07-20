class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = [-1] * len(nums)
        def dfs(i):
            if i >= len(nums) - 1:
                return True

            if nums[i] == 0:
                return False
            
            if cache[i] != -1:
                return cache[i]
            
            for j in range(nums[i], 0, -1):
                if dfs(i+j):
                    cache[i] = True
                    return cache[i]
             
            cache[i] = False
            return cache[i]
        return dfs(0)
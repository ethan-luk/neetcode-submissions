class Solution:
    def jump(self, nums: List[int]) -> int:
        
        cache = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums) - 1:
                return 0
            if nums[i] == 0:
                return float('inf')
            if cache[i] != -1:
                return cache[i]
            
            cache[i] = float('inf')
            for j in range(nums[i], 0, -1):
                cache[i] = min(cache[i], 1 + dfs(i+j))
            return cache[i]
            
        return dfs(0)

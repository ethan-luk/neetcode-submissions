class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2
        
        def dfs(i, total):
            if i >= len(nums):
                return total == target
            if total == target:
                return True
            
            if total > target:
                return False
            
            return dfs(i+1, total + nums[i]) or dfs(i+1, total)
        
        return dfs(0, 0)
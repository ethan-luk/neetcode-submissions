class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        def dfs(i, cur_sum):
            if i == len(nums):
                return cur_sum == target
            
            return dfs(i+1, cur_sum + nums[i]) + dfs(i+1, cur_sum - nums[i])
        
        return dfs(0, 0)
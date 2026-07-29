class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * (len(nums) + 1)
        dp[len(nums) - 1] = True

        for i in range(len(nums) - 2, -1, -1):
            end = min(len(nums), i + nums[i] + 1)
            for j in range(i + 1, end):
                if dp[j] == True:
                    dp[i] = True
                    break
        
        return dp[0]
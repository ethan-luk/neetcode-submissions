class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def dfs(i):
            if i >= len(nums) - 1:
                return True

            if nums[i] == 0:
                return False
            
            # Greedily try the largest jump first to reach the end faster
            # and help stay within recursion limits for specific cases.
            for j in range(nums[i], 0, -1):
                if dfs(i+j):
                    return True
            return False
        
        # Increase recursion limit for deep test cases as requested without memoization
        sys.setrecursionlimit(2000)
        return dfs(0)
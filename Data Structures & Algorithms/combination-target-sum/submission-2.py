class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            # base case 1: total == target
            if total == target:
                res.append(curr.copy())
                return
            
            # base case 2: total is greater than the target or out of index
            if i >= len(nums) or total > target:
                return

            # add number
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])

            # don't add next number
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res

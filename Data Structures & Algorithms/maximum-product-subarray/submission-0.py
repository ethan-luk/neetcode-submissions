class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1, 1

        for num in nums:
            if num == 0:
                curMax, curMin = 1, 1
                continue
            
            temp = curMax * num
            curMax = max(curMax * num, curMin * num, num)
            curMin = min(temp, curMin * num, num)
            res = max(curMax, res)

        return res
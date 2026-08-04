class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return 0

        curMax = nums[0]
        count = 0
        for num in nums:
            if num == curMax:
                count += 1
            else:
                count -= 1
            
            if count < 0:
                curMax = num
                count = 1
        
        return curMax
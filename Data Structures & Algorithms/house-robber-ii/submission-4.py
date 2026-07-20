class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        if len(nums) == 1:
            return nums[0]

        one, two = 0, 0
        
        for i in range(len(nums)):
            temp = two
            two = max(two, one + nums[i])
            one = temp
        
        return two
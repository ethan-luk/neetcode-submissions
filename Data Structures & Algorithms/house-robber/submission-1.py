class Solution:
    def rob(self, nums: List[int]) -> int:

        one, two = 0, 0
        for i in range(len(nums)):
            temp = two
            two = max(one + nums[i], two)
            one = temp
        
        return two
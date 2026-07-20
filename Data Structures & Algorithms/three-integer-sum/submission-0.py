class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two pointers
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            l, r = i+1, len(nums) - 1
            while l < r:
                s = num + nums[l] + nums[r]
                if s == 0:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        
        return res
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1, len(nums)):
                if j > i + 1 and nums[j] == nums[j-1]: continue
                for k in range(j+1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k-1]: continue
                    val = target - nums[i] - nums[j] - nums[k]
                    l, r = k + 1, len(nums) - 1
                    while l <= r:
                        m = l + (r - l) // 2
                        if nums[m] == val:
                            res.append([nums[i], nums[j], nums[k], nums[m]])
                            break
                        elif nums[m] < val: 
                            l = m + 1
                        else:
                            r = m - 1
        
        return res
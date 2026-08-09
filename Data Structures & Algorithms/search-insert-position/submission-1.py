class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                if m == len(nums) - 1 or nums[m+1] > target:
                    return m + 1
                else:
                    l = m + 1
        return 0
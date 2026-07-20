class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        min_index = l
        l, r = 0, len(nums) - 1
        if nums[min_index] <= target and target <= nums[r]:
            l = min_index
        else:
            r = min_index - 1
        
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1
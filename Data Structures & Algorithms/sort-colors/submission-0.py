class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i, num in enumerate(nums[1:], 1):
            cur = i - 1
            val = nums[i]
            while cur >= 0 and nums[cur] > val:
                nums[cur+1] = nums[cur]
                cur -= 1
            nums[cur+1] = val
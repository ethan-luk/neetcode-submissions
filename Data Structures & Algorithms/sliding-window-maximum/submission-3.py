class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = [] # (nums[i], i)

        for i, num in enumerate(nums):
            heapq.heappush(window, (-num, i))

            while window[0][1] <= i - k:
                heapq.heappop(window)
            
            if i >= k - 1:
                res.append(-window[0][0])
        
        return res
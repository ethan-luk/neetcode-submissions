class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freqs = [[] for i in range(len(nums) + 1)]

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for num, freq in counts.items():
            freqs[freq].append(num)
        
        res = []
        for i in range(len(freqs) - 1, 0, -1):
            for num in freqs[i]:
                res.append(num)
                if len(res) == k:
                    return res
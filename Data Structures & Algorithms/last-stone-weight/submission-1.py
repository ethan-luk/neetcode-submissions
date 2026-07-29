class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            largest = heapq.heappop(stones)
            second_largest = heapq.heappop(stones)
            if largest == second_largest:
                continue
            heapq.heappush(stones, abs(largest - second_largest) * -1)
        
        return abs(stones[0]) if stones else 0
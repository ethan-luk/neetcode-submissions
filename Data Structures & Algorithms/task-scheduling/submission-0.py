class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-t for t in count.values()]
        heapq.heapify(maxHeap)
        q = deque() # [-count, idle time]
        time = 0

        while maxHeap or q:
            time += 1
            if maxHeap:
                c = 1 + heapq.heappop(maxHeap)
                if c:
                    q.append((c, time + n))
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time


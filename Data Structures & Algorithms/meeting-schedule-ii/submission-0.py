class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda i: i.start)
        rooms = []
        for interval in intervals:
            start, end = interval.start, interval.end
            if rooms and start >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, end)
        return len(rooms)
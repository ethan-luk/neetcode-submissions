class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        stack = []

        for interval in intervals:
            start, end = interval.start, interval.end
            if len(stack) > 0 and start < stack[-1]:
                return False
            stack.append(end)
        return True
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        res = 0

        # [(7, 1), (4, 2), (1, 2), (0, 1)]
        for p, s in pair:
            time_taken = (target - p) / s
            stack.append(time_taken)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)

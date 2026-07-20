class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while len(stack) > 0 and temp > stack[-1][1]:
                old_index, old_temp = stack.pop()
                res[old_index] = i - old_index            
            stack.append((i, temp))

        return res
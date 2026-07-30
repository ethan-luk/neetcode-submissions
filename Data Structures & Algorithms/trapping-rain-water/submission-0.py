class Solution:
    def trap(self, height: List[int]) -> int:
        # w[i] = min(leftMax, rightMax) - h[i]

        leftMax, rightMax = [], []

        curMax = 0
        for i in range(len(height)):
            newMax = max(curMax, height[i])
            leftMax.append(newMax)
            curMax = newMax

        curMax = 0
        for i in range(len(height) - 1, -1, -1):
            newMax = max(curMax, height[i])
            rightMax.append(newMax)
            curMax = newMax
        
        rightMax = rightMax[::-1]

        res = 0
        for i in range(len(height)):
            res += (min(leftMax[i], rightMax[i]) - height[i])
        
        return res
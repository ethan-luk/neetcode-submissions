class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s)):
            if dp[i] == False:
                continue
            
            for j in range(i + minJump, min(i + maxJump, len(s) - 1) + 1):
                if s[j] == '0':
                    dp[j] = True
        
        return dp[len(s) - 1]

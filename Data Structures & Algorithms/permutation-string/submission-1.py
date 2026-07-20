class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_d = {}
        for c in s1:
            s1_d[c] = s1_d.get(c, 0) + 1
        
        for i in range(len(s2) - len(s1) + 1):
            window_d = {}
            for c in s2[i:i+len(s1)]:
                window_d[c] = window_d.get(c, 0) + 1
            if window_d == s1_d:
                return True
            
        
        return False
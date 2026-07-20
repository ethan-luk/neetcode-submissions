class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_d = {}
        for c in s1:
            s1_d[c] = s1_d.get(c, 0) + 1
        
        window_d = {}

        for i in range(len(s1)):
            window_d[s2[i]] = window_d.get(s2[i], 0) + 1

        for i in range(len(s2) - len(s1) + 1):
            if all(window_d.get(k, 0) == v for k, v in s1_d.items()):
                return True
            
            if i + len(s1) < len(s2):
                window_d[s2[i+len(s1)]] = window_d.get(s2[i+len(s1)], 0) + 1
                window_d[s2[i]] = window_d.get(s2[i], 0) - 1
        
        return False
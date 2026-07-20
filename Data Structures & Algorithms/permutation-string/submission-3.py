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

        l, r = 0, len(s1) - 1
        while r < len(s2):
            if window_d == s1_d:
                return True
            
            window_d[s2[l]] = window_d.get(s2[l], 0) - 1
            if window_d[s2[l]] == 0: del window_d[s2[l]]
            l += 1
            r += 1
            if r < len(s2):
                window_d[s2[r]] = window_d.get(s2[r], 0) + 1

        return False
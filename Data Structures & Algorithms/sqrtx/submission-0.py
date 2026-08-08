class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        while l <= r:
            m = l + (r - l) // 2
            m_sq = m * m
            if m_sq == x:
                return m
            elif m_sq < x:
                l = m + 1
            else:
                r = m - 1
        
        return r
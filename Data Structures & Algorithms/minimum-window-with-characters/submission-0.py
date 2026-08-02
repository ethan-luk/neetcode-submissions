class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # We have a dictionary that has all the counts each 
        # char in t, sliding window, extend if we dont have
        # all the chars we need, shrink if we do

        tCount = Counter(t)
        sCount = {}

        have = 0
        need = len(tCount)

        l = 0
        res = ""
        for r in range(len(s)):
            if s[r] in tCount:
                sCount[s[r]] = sCount.get(s[r], 0) + 1
                if sCount[s[r]] == tCount[s[r]]:
                    have += 1
            while have == need:
                if not res or (r - l + 1) < len(res):
                    res = s[l:r+1]
                # shrink
                if s[l] in tCount:
                    sCount[s[l]] -= 1
                    if sCount[s[l]] < tCount[s[l]]:
                        have -= 1
                l += 1


        return res
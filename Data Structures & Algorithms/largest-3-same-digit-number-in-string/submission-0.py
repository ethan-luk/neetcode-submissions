class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] and num[i] == num[i + 2]:
                if res == "" or int(num[i]) > int(res[0]):
                    res = num[i] * 3
        
        return res
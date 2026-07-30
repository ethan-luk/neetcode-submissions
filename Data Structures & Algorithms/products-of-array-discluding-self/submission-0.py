class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 1, 2, 8, 48]
        # [1, 6, 24, 48, 48]
        # [48, 48, 24, 6, 1]
            # [ 1, 1, 2, 8, 48]
        
        prefixProduct = [1]
        postfixProduct = [1]

        curProd = 1
        for num in nums:
            curProd *= num
            prefixProduct.append(curProd)
        
        curProd = 1
        for num in nums[::-1]:
            curProd *= num
            postfixProduct.append(curProd)
        
        postfixProduct = postfixProduct[::-1]

        res = []
        for i in range(1, len(postfixProduct)):
            res.append(postfixProduct[i] * prefixProduct[i-1])
        
        return res

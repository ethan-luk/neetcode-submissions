class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i, curr_set):
            # Base case 1: len(curr_set) == k, then we can add it to the result and return
            if len(curr_set) == k:
                res.append(curr_set.copy())
                return
            
            # Base case 2: We ran out of numbers, return
            if i > n:
                return


            # Choose to add next number
            curr_set.append(i)
            dfs(i + 1, curr_set)
            
            # Don't choose to add next number
            curr_set.pop()
            dfs(i + 1, curr_set)
        
        dfs(1, [])
        return res
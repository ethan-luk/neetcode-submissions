class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visited = set()

        def dfs(node):
            for nei in adjList[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        res = 0
        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                res += 1
        
        return res

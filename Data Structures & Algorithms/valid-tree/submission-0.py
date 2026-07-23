class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Valid if no cycles and fully connected

        adjList = defaultdict(list)
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        

        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in adjList[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            
            return True

        return dfs(0, -1) and len(visited) == n
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjlist = [ [] for _ in range(n)]
        for [src, dst] in edges:
            adjlist[src].append(dst)
            adjlist[dst].append(src)
        
        visited = [0]*n
        def dfs(s):
            visited[s] = 1
            for neighbor in adjlist[s]:
                if visited[neighbor] == 0:
                    dfs(neighbor)

        component = 0
        for v in range(n):
            if visited[v] == 0:
                component += 1
                dfs(v)
        return component
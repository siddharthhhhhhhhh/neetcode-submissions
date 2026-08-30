class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        visited = set()
        def dfs(node, parent):
            visited.add(node)
            for x in graph[node]:
                if x == parent:
                    continue
                if x in visited:
                    continue
                dfs(x, node)
            return
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i,-1)
                count += 1
        return count
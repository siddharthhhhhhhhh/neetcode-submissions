class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(1, len(edges)+1)}
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        visited = []
        list1 = []
        def dfs(node, parent):
            if node in visited:
                list1.append(node)
                list1.append(parent)
                list1.append(visited[-2])
                return
            visited.append(node)
            for x in graph[node]:
                if x == parent:
                    continue
                dfs(x, node)                  
            visited.remove(node)
            return
        dfs(1, -1)
        for i in range(len(edges)):
            a,b = edges[len(edges)-i-1]
            if a in list1 and b in list1:
                return [a,b]
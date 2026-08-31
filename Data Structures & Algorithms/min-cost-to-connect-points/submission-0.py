class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distances = []
        parent = list(range(len(points)+1))
        rank = [0]*len(points)
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(u,v):
            rx, ry = find(u), find(v)
            if rx==ry:
                return False
            if rank[rx] < rank[ry]:
                ry, rx = rx, ry
            parent[ry] = rx
            if rank[ry] == rank[rx]:
                rank[rx] += 1
            return True
            
            
        for i in range(len(points)):
            for j in range(len(points)):
                if points[i] == points[j]:
                    continue
                x1, x2 = points[i]
                x3, x4 = points[j]
                dist = abs(x3-x1) + abs(x4-x2)
                distances.append([dist, i, j])
        distances.sort()
        res = 0
        for c, u, v in distances:
            if union(u,v):
                res += c
        return res
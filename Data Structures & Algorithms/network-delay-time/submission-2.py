class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {}
        heap = [(0, k)]  

        while heap:
            d, node = heapq.heappop(heap)
            if node in dist:
                continue  
            dist[node] = d
            for neighbor, weight in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(heap, (d + weight, neighbor))

        if len(dist) != n:
            return -1
        return max(dist.values())
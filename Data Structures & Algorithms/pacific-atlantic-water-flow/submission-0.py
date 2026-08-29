class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(starts):
            visited = set(starts)
            q = deque(starts)
            while q:
                row, col = q.popleft()
                val = heights[row][col]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (0 <= r < rows and 0 <= c < cols
                            and (r, c) not in visited
                            and heights[r][c] >= val):
                        visited.add((r, c))
                        q.append((r, c))
            return visited

        pacific_starts = [(0, j) for j in range(cols)] + [(i, 0) for i in range(rows)]
        atlantic_starts = [(rows - 1, j) for j in range(cols)] + [(i, cols - 1) for i in range(rows)]

        pacific_reachable = bfs(pacific_starts)
        atlantic_reachable = bfs(atlantic_starts)

        return [[r, c] for r, c in pacific_reachable & atlantic_reachable]
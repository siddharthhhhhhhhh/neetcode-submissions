class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    visited.add((i, j))
                    q.append((i, j))
            distance = 0
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while q:
                distance += 1
                for _ in range(len(q)):
                    row, col = q.popleft()
                    for dr, dc in directions:
                        r = row + dr
                        c = col + dc
                        if (r in range(len(grid))) and (c in range(len(grid[0]))) and ((r, c) not in visited) and (grid[r][c] != -1):
                            q.append((r, c))
                            visited.add((r, c))
                            grid[r][c] = distance
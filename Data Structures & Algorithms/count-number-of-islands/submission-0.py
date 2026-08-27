class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        island = 0
        def bfs(i, j):
            q = deque()
            q.append((i, j))
            visited.add((i, j))
            while q:
                directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row+dr
                    c = col+dc
                    if (r in range(len(grid))) and (c in range(len(grid[0]))) and ((r,c) not in visited) and (grid[r][c] == "1"):
                        q.append((r,c))
                        visited.add((r,c))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i, j)
                    island += 1
        return island
        
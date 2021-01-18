class Solution(self):
    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        visited = {}

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    self.BFS(i, j, rows, cols, grid, visited)
        
        return count

    def isSafe(self, x, y, rows, cols, grid, visited):
        return (0 <= x < rows) and (0 <= y < cols) and grid[x][y] == '1' and ((x,y) not in visited)

    def BFS(self, i, j, rows, cols, grid, visited):
        queue = [(i, j)]
        visited[(i, j)] = True
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]

        while len(queue) > 0:
            l = len(queue)

            for _ in range(l):
                x, y = queue.pop(0)

                for i in range(4):
                    if self.isSafe(x+dx[i], y+dy[i], rows, cols, grid, visited):
                        queue.append((x+dx[i], y+dy[i]))
                        visited[(x+dx[i], y+dy[i])] = True

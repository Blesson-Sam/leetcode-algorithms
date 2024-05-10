class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        h, w = len(grid), len(grid[0])
        res = 0
        for y in range(h):
            for x in range(w):
                if grid[y][x] == '1':
                    stack = [(x, y)]
                    res += 1     
                    while stack:
                        X, Y = stack.pop()
                        grid[Y][X] = '0'
                        for i,j in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                            XX = max(min(X + i, w - 1), 0)
                            YY = max(min(Y + j, h - 1), 0)
                            if grid[YY][XX] == '1':
                                stack.append((XX, YY))
                        


        return res
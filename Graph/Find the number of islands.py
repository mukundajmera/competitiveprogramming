# sys.setrecursionlimit(900000000)

import sys

sys.setrecursionlimit(100000)


class Solution:
    def isSafe(self, n, m, i, j):
        return (i >= 0 and i < m and
                j >= 0 and j < n and
                self.visited[i][j] == False and self.grid[i][j] == '1')

    def dfs(self, n, m, i, j):
        self.visited[i][j] = True
        # Recur for all connected neighbours
        rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1];
        colNbr = [-1, 0, 1, -1, 1, -1, 0, 1];
        for k in range(8):
            if self.isSafe(n, m, i + rowNbr[k], j + colNbr[k]):
                self.dfs(n, m, i + rowNbr[k], j + colNbr[k])

    def numIslands(self, grid1):
        # Code here
        n = len(grid1[0])
        m = len(grid1)
        self.grid = grid1
        self.visited = []
        for row in range(m):
            self.visited.append([False] * n)
        res = 0
        for i in range(m):
            for j in range(n):
                val = self.grid[i][j]
                if self.grid[i][j] == '1' and self.visited[i][j] == False:
                    res += 1
                    self.dfs(n, m, i, j)

        return res


# {
#  Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = map(int, input().split())
        grid = []
        for _ in range(n):
            a = list(input().split())
            grid.append(a)
        obj = Solution()
        ans = obj.numIslands(grid)
        print(ans)

# } Driver Code Ends
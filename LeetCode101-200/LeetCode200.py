class Solution(object):
    # 本题采用深度优先遍历方法
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # 记录岛屿的数量
        island_count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    island_count += 1
                    dfs(row, col)


        def dfs(row, col):
            if row not in range(len(grid)) or col not in range(len(grid[0]))
                or grid[row][col] == 0:
                return
            grid[row][col] == 0
            # 上下左右四个方向遍历
            dfs(row, col-1)
            dfs(row+1, col)
            dfs(row, col+1)
            dfs(row-1, col)

        return island_count


if __name__ == "__main__":
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],
            ["1","1","0","0","0"],["0","0","0","0","0"]]
    print(Solution().numIslands(grid))

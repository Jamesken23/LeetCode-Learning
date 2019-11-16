class Solution(object):
    # 可使用深度优先搜索（DFS）求解
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # 判断给定区域是否为空
        if len(board) ==0 or len(board[0]) == 0:
            return
        # 获取行列值
        rows = len(board)
        cols = len(board[0])
        # 从第一列和最后一列依次往中间做深度遍历，看区域中是否有与边缘列相连的"0"
        # 如果存在这样的"0"，将其变成"*"，最后我们是要将其变成"0"的
        for row in range(rows):
            if board[row][0] == "O":
                self.dfs(board, row, 0)
            if board[row][cols-1] == "O":
                self.dfs(board, row, cols-1)
        for col in range(cols):
            if board[0][col] == "O":
                self.dfs(board, 0, col)
            if board[rows-1][col] == "O":
                self.dfs(board, rows-1, col)
        print(board)
        # 标记为"*"的就要重新变成"0"了，仍然为"0"的则要变成"X"了
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "*":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"
        

    # 深度遍历搜索
    def dfs(self, board, row, col):
        if row not in range(0,len(board)) or col not in range(0,len(board[0])) or board[row][col] != "O":
            return
        board[row][col] = "*"
        # 遍历上下左右四个方向
        self.dfs(board, row-1, col)
        self.dfs(board, row, col+1)
        self.dfs(board, row+1, col)
        self.dfs(board, row, col-1)

if __name__ == "__main__":
    board = [["X","O","X"],["O","X","O"],["X","O","X"]]
    Solution().solve(board)

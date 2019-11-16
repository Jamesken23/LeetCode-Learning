class Solution(object):
    # 本题可使用动态规划法解决
    # 从倒数第二行开始依次遍历，最后triangle[0][0]即是我们想要的结果
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0:
            return 0
        row = len(triangle) - 2
        for row in range(row, -1, -1):
            for col in range(len(triangle[row])):
                triangle[row][col] += min(triangle[row+1][col],triangle[row+1][col+1])
        return triangle[0][0]

    
if __name__ == "__main__":
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    min_sum = Solution().minimumTotal(triangle)
    print(min_sum)

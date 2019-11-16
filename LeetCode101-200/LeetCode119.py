class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        yanghui_list = [[1]]
        for row in range(1, rowIndex+1):
            single_row = []
            for col in range(row+1):
                lastrow_length = len(yanghui_list[row-1])
                left = yanghui_list[row-1][col-1] if col-1 in range(lastrow_length) else 0
                right = yanghui_list[row-1][col] if col in range(lastrow_length) else 0
                single_row.append(left+right)
            yanghui_list.append(single_row)
        return yanghui_list[rowIndex]


if __name__ == "__main__":
    rowIndex = 3
    target_row = Solution().getRow(rowIndex)
    print(target_row)

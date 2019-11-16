class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        yanghui_list = [[1]]
        if numRows == 0:
            return []
        for row in range(1, numRows):
            single_row = []
            for col in range(row+1):
                lastrow_length = len(yanghui_list[row-1])
                left = yanghui_list[row-1][col-1] if col-1 in range(lastrow_length) else 0
                right = yanghui_list[row-1][col] if col in range(lastrow_length) else 0
                single_row.append(left+right)
            yanghui_list.append(single_row)
        return yanghui_list


if __name__ == "__main__":
    numRows = 5
    yanghui = Solution().generate(numRows)
    print(yanghui)

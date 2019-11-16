class Solution(object):
    # 核心点：将格雷编码与二进制编码联系起来
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        gray_list = []
        for index in range(2**n):
            left_index = index >> 1
            gray = index ^ left_index
            gray_list.append(gray)
        return gray_list


if __name__ == "__main__":
    n = 0
    gray_list = Solution().grayCode(n)
    print(gray_list)

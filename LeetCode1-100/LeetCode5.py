class Solution(object):
    # 此题采用动态规划的方法
    # 比较发现：还是将标记矩阵的值设为布尔值最好，方便递归判断
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        # 首先给标记矩阵初始化，即设置为全False矩阵
        flag_matrix = []
        for s_index in range(len(s)):
            flag_matrix.append([False]*len(s))
        # 设置取得最大回文子串的下标起始值和终点值
        max_start = 0
        max_end = 0
        # 两层for循环来更新标记矩阵的值
        for end in range(len(s)):
            for start in range(end+1):
                if s[end] == s[start]:
                    if end-1 > start+1:
                        flag_matrix[end][start] = flag_matrix[end-1][start+1]
                    else:
                        flag_matrix[end][start] = True
                else:
                    flag_matrix[end][start] = False
                if flag_matrix[end][start] > 0:
                    if end-start > max_end-max_start:
                        max_start = start
                        max_end = end
        print(flag_matrix)
        return s[max_start:max_end+1]


if __name__ == "__main__":
    s = "aba"
    max_s = Solution().longestPalindrome(s)
    print(max_s)

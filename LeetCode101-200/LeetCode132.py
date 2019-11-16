class Solution(object):
    # 本题采用动态规划方法，回溯法超出时间限制了
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """   
        if len(s) <= 1:
            return 0
        # 定义标记列表
        record = [index for index in range(-1, len(s))]
        for end in range(1, len(s)+1):
            for start in range(end):
                if s[start:end] == s[start:end[::-1]:
                    record[end]=record[start]
                    break
        return record

if __name__ == "__main__":
    s = "aab"
    min_split = Solution().minCut(s)
    print(min_split)

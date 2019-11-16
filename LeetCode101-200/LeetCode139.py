class Solution(object):
    # 本题回溯法超出时间限制，采用动态回归法
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 初始化标记列表
        flag = [True]+[False]*len(s)

        for start in range(len(s)):
            if flag[start]:
                for end in range(start+1, len(s)+1):
                    if s[start:end] in wordDict:
                        flag[end] = True
        return flag[-1]


if __name__ == "__main__":
    s = "aaaaaaa"
    wordDict = ["aaaa","aaa"]
    flag = Solution().wordBreak(s, wordDict)
    print(flag)

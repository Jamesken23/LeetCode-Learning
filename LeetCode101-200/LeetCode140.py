class Solution(object):
    # 本题采用回溯法
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if len(s) == 0 or len(wordDict) == 0:
            return []
        max_length = max([len(word) for word in wordDict])
        # 定义一列表用来保存最终的分割结果
        split_s = []

        def back(s, sub_str_list=[]):
            if not s:
                new_str = " ".join(sub_str_list)
                split_s.append(new_str)
            for start in range(len(s)):
                sub_str = s[:start+1]
                if start < max_length and sub_str in wordDict:
                    back(s[start+1:], sub_str_list+[sub_str])

        back(s)
        return split_s
                

if __name__ == "__main__":
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    split_s = Solution().wordBreak(s, wordDict)
    print(split_s)

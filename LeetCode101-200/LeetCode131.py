class Solution(object):
    # 本题采用回溯法
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        split_result = []
        if len(s) == 0:
            return split_result

        def back(start=0, res=[]):
            if start >= len(s):
                split_result.append(res)
                return 
            for end in range(start+1, len(s)+1):
                split_s = s[start:end]
                if split_s == s[start:end][::-1]:
                    back(end, res+[split_s])

        back()
        return split_result
            

if __name__ == "__main__":
    s = "a"
    split_result = Solution().partition(s)
    print(split_result)

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_list = list(s)
        new_s_list = [index.lower() for index in s_list if index.isalpha() or index.isdigit()]
        return True if new_s_list == new_s_list[: : -1] else False


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    result = Solution().isPalindrome(s)
    print(result)

class Solution(object):
    # 本题采用回溯法解决
    # 注意点：IP地址空缺位不补0
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # 定义包含所有可能的IP地址的列表
        address_list = []
        if len(s) < 4 or len(s) > 12:
            return address_list

        # 核心的递归算法
        def back(address=[], s=s):
            if len(address) == 4 and len(s) == 0:
                address_str = ".".join(address)
                if address_str not in address_list:
                    address_list.append(address_str)
                return
            for index in range(3):
                if len(s) >= index+1:
                    one_str = s[:index+1]
                    # 若出现"010010"情况，对于0的取舍需要着重考虑
                    # 关键一条就是：切割完的IP地址长度与原地址长度相等
                    if int(one_str) in range(256) and str(int(one_str)) == one_str:
                        one_str = str(int(one_str))
                        back(address+[one_str], s[index+1:])

        back()
        return address_list


if __name__ == "__main__":
    s = "010010"
    address = Solution().restoreIpAddresses(s)
    print(address)

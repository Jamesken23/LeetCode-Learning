class Solution(object):
    # 可用count(num)查找列表nums中单个元素num在列表nums中的个数情况
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_nums = set(nums)
        return 2*sum(set_nums)-sum(nums)


if __name__ == "__main__":
    nums = [2, 3, 2]
    unique_num = Solution().singleNumber(nums)
    print(unique_num)

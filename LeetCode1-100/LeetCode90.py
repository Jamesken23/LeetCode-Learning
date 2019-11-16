class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 首先将nums数组排序，方便后续去重
        nums.sort()
        # 定义保存所有子集的集合
        combine_set = []

        # 核心的递归算法
        def back(start=0, current_list=[]):
            """
            :start: 每次递归时的起点值
            :current_list: 保存临时子集的集合
            """
            if current_list not in combine_set:
                combine_set.append(current_list)
            for index in range(start, len(nums)):
                back(index+1, current_list+[nums[index]])
        back()
        return combine_set


if __name__ == "__main__":
    nums = [4,4,4,1,4]
    combine_set = Solution().subsetsWithDup(nums)
    print(combine_set)

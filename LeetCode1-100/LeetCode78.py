class Solution(object):
    # 本题亦可使用回溯法
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 定义保存所有子集的集合
        combine_list = []

        # 核心的递归算法
        def back(start=0, current_list=[]):
            """
            :start: 每次递归时的起点值
            :current_list: 保存临时子集的集合
            """
            combine_list.append(current_list)
            for index in range(start, len(nums)):
                back(index+1, current_list+[nums[index]])
        back()
        return combine_list


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    combine_list = Solution().subsets(nums)
    print(combine_list)

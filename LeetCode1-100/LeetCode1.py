class Solution(object):
    # 可用一遍遍历，即根据当前遍历得到的元素index，
    # 查找target-index是否在剩余数组里出现
    # 如果找得到，则返回其下标值；反之则说明没有该答案
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer = []
        for left_index in range(len(nums)):
            right = target - nums[left_index]
            if right in nums[left_index+1:]:
                nums_right = nums[left_index+1:]
                right_index = nums_right.index(right)+left_index+1
                answer.extend([left_index, right_index])
                break
        return answer


if __name__ == "__main__":
    nums = [-1, -2, -3, -4, -5]
    target = -8
    answer = Solution().twoSum(nums, target)
    print(answer)

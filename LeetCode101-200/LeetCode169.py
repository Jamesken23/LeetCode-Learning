class Solution(object):
    # 摩尔投票法
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority = nums[0]
        count = 1

        for index in range(1, len(nums)):
            if count == 0:
                majority = nums[index]
                
            count = count+1 if majority == nums[index] else count-1
        return majority
                

if __name__ == "__main__":
    nums = [3, 2, 3]
    mode = Solution().majorityElement(nums)
    print(mode)

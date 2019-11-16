class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        true_k = k%len(nums)
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]
        return nums

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    move_nums = Solution().rotate(nums, k)
    print(move_nums)

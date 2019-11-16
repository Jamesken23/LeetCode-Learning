class Solution(object):
    # 此种解法思路就是先将两个列表中的元素合并，然后统一排序
    # 按照新列表的长度的奇偶情况来查找中位数
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 将两个列表中的元素合并，然后统一排序
        nums1.extend(nums2)
        nums1.sort()
        # 根据除2的余数情况来决定该取中间两个元素还是一个元素
        mid_index = len(nums1)//2
        yushu = len(nums1)%2
        mid_num = 0.0
        if yushu == 0:
            mid_num = float(nums1[mid_index-1]+nums1[mid_index])/2
        else:
            mid_num = nums1[mid_index]
        return mid_num


if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]
    mid_num = Solution().findMedianSortedArrays(nums1, nums2)
    print(mid_num)

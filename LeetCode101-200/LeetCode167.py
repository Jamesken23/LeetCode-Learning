class Solution(object):
    # 双指针从两端往中间逼近
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 定义一列表专门用来保存结果集
        index_list = []
        # 分别定义首尾指针
        start = 0
        end = len(numbers)-1
        while start<end:
            if numbers[start] + numbers[end] == target:
                index_list.extend([start+1, end+1])
                break
            elif numbers[start] + numbers[end] > target:
                end -= 1
            else:
                start += 1
        return index_list
        

if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    index_list = Solution().twoSum(numbers, target)
    print(index_list)

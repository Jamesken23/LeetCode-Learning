class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 本题还可先将链表转化为数组，再用108题方法
     def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return
        head_list = []
        while head:
            head_list.append(head.val)
            head = head.next
        # 调用和第108题一样的动态规划方法
        def buildBST(nums):
            if len(nums)==0:
                return
            # 取nums列表的中间下标值
            mid_index = len(nums)//2
            pNode = TreeNode(nums[mid_index])
            pNode.left = buildBST(nums[:mid_index])
            pNode.right = buildBST(nums[mid_index+1:])
            return pNode
        return buildBST(head_list)


if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]
    head = ListNode(0)
    head_copy = head
    for index in nums:
        head_copy.next = ListNode(index)
        head_copy = head_copy.next
    BTree = Solution().sortedListToBST(head.next)
    print(BTree)

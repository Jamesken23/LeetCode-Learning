class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_list = []
        l2_list = []
        l1_copy = l1
        l2_copy = l2
        #首先分别获取l1和l2链表上节点值     
        while l1_copy:
           l1_list.append(l1_copy.val)
           l1_copy = l1_copy.next
        while l2_copy:
           l2_list.append(l2_copy.val)
           l2_copy = l2_copy.next
        #分别在l1_list与l2_list列表末尾补0，使之长度相等，便于计算
        max_length = max(len(l1_list), len(l2_list))
        l1_list.extend([0]*(max_length+1-len(l1_list)))
        l2_list.extend([0]*(max_length+1-len(l2_list)))
        #遍历l1_list与l2_list列表，对相应元素做加法运算
        l_list = []
        #定义两数相加是否超过10导致的进位
        jinwei = 0
        for l_index in range(max_length+1):
            two_sum = l1_list[l_index] + l2_list[l_index] + jinwei
            if two_sum < 10:
                l_list.append(two_sum)
                jinwei = 0
            else:
                jinwei = two_sum//10
                l_list.append(two_sum%10)
        #如果l_list长度大于1且末尾元素为0，说明最后一位没有进位
        if len(l_list)>1 and l_list[-1] == 0:
            l_list.pop()
        print("l_list", l_list)
        #最后将两数相加的结果赋值给一链表
        l = ListNode(0)
        l_copy = l
        for l_index in l_list:
            l_copy.next = ListNode(l_index)
            l_copy = l_copy.next
        return l.next


if __name__ == "__main__":
    l1_list = [2, 4, 3]
    l2_list = [5, 6, 4]
    l1 = ListNode(0)
    l1_copy = l1
    for l1_index in l1_list:
        l1_copy.next = ListNode(l1_index)
        l1_copy = l1_copy.next
    l2 = ListNode(0)
    l2_copy = l2
    for l2_index in l2_list:
        l2_copy.next = ListNode(l2_index)
        l2_copy = l2_copy.next
    final_listnode = Solution().addTwoNumbers(l1.next, l2.next)
    print(final_listnode)

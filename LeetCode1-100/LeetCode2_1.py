class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 直接对两个链表操作；对应节点上的值做加法运算，过10则进位。位数不够则补0
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = ListNode(0)
        l_copy = l
        # 定义两数相加是否大于10进位
        carry = 0
        while l1 or l2:
            # 因为l1与l2链表对应的位数可能不同，此时需要将空缺的位置补0
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            two_sum = l1_val + l2_val + carry
            if two_sum < 10:
                l_copy.next = ListNode(two_sum)
                carry = 0
            else:
                carry = two_sum//10
                l_copy.next = ListNode(two_sum%10)
            l_copy = l_copy.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry > 0:
            l_copy.next = ListNode(carry)
        return l.next


if __name__ == "__main__":
    l1_list = [2, 4, 3]
    l2_list = [5, 6]
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

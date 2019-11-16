class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        head_copy = head
        head_list = []
        # 首先将head链表中各节点的值保存至head_list数组中
        while head_copy:
            head_list.append(head_copy.val)
            head_copy = head_copy.next
        # 直接将head_list数组中[m-1:n]位置的数反转
        head_list[m-1:n] = head_list[m-1:n][::-1]
        reverse_head = ListNode(0)
        reverse_head_copy = reverse_head
        # 最后将反转之后的head_list数组中元素赋值给新链表
        for head_num in head_list:
            reverse_head_copy.next = ListNode(head_num)
            reverse_head_copy = reverse_head_copy.next
        return reverse_head.next


if __name__ == "__main__":
    head_list = [1, 2, 3, 4]
    head = ListNode(0)
    head_copy = head
    for head_num in head_list:
        head_copy.next = ListNode(head_num)
        head_copy = head_copy.next
    m = 1
    n = 4
    reverse_head = Solution().reverseBetween(head.next, m, n)
    while reverse_head:
        print(reverse_head.val)
        reverse_head = reverse_head.next
    print(reverse_head)

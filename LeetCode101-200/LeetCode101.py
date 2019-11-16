class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 本题关键是：中序遍历这棵树得到的序列为回文数
    # 注意：遍历事不能将NOne空值去掉，否则顺序会有混淆
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isSameTree(root.left, root.right)

    def isSameTree(self, p, q):
        if p is not None and q is not None:
            if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                return True
            else:
                return False
        elif p is None and q is None:
            return True
        else:
            return False
            

    def createBTree(self, data, index=0):
        if len(data) == 0:
            return
        pNode = None
        if index < len(data):
            pNode = TreeNode(data[index])
            pNode.left = self.createBTree(data, 2*index+1)
            pNode.right = self.createBTree(data, 2*index+2)
        return pNode


if __name__ == "__main__":
    root_list = [1,2,3,3,None,2,None]
    root = Solution().createBTree(root_list)
    result = Solution().isSymmetric(root)
    print(result)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 此题可用递归法遍历得到整棵树的深度
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0

    def createBTree(self, data, index=0):
        pNode = None
        if index < len(data):
            pNode = TreeNode(data[index])
            pNode.left = self.createBTree(data, 2*index+1)
            pNode.right = self.createBTree(data, 2*index+2)
        return pNode


if __name__ == "__main__":
    data = [3, 9, 20, None, None, 15, 7]
    root = Solution().createBTree(data)
    max_depth = Solution().maxDepth(root)
    print(max_depth)

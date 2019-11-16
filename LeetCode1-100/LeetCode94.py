class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root == None:
            return result
        
        stack = []
        while stack or root:
            if root != None:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                result.append(root.val)
                root = root.right

        return result

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
    data = [1, None, 2, 3]
    two_tree = Solution().createBTree(data)
    tree = Solution().inorderTraversal(two_tree)
    print(tree)

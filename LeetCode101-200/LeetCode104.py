class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 此题可用层次遍历整棵树的深度
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 定义二叉树的最大深度
        max_depth = 0
        # 该列表用来保存当前遍历的一层的节点
        current_nodes = [root]
        if root:
            max_depth += 1
            while current_nodes:
                next_nodes = []
                for node in current_nodes:
                    if node.left and node.left.val is not None:
                        next_nodes.append(node.left)
                    if node.right and node.right.val is not None:
                        next_nodes.append(node.right)
                if next_nodes:
                    max_depth += 1
                current_nodes = next_nodes
        return max_depth

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

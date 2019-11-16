class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 本题就是在102题的基础上逆序输出即可
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 定义列表用来保存层次遍历的数据
        root_data = []
        # 用来保存每一层的节点
        nodes_list = [root]
        while nodes_list:
            # 用来保存每一层节点的val值
            level_val = []
            # 用来保存下一层节点
            next_nodes = []
            for node in nodes_list:
                level_val.append(node.val)
                if node.left and node.left.val is not None:
                    next_nodes.append(node.left)
                if node.right and node.right.val is not None:
                    next_nodes.append(node.right)
            nodes_list = next_nodes
            root_data.append(level_val)
        root_data.reverse()
        return root_data

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
    print(Solution().levelOrderBottom(root))

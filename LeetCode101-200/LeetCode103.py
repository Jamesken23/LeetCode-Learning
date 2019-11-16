class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 用来保存锯齿形层次遍历二叉树的结果
        root_list = []
        if root:
            # 用来保存每一层节点
            node_list = [root]
            # 判断是否逆序遍历的标志
            is_reverse = False
            while node_list:               
                # 用来保存每一层节点对应的val值
                level_data = []
                # 用来暂时保存下一层节点
                next_nodes = []
                for node in node_list:
                    level_data.append(node.val)
                    if node.left and node.left.val is not None:
                        next_nodes.append(node.left)
                    if node.right and node.right.val is not None:
                        next_nodes.append(node.right)
                if is_reverse is True:
                    level_data.reverse()
                is_reverse = not is_reverse
                root_list.append(level_data)
                node_list = next_nodes
        return root_list

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
    root_list = Solution().zigzagLevelOrder(root)
    print(root_list)

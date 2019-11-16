class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 该列表用来保存层次遍历的最终结果
        pre_list = []    
        # 该列表用来保存每一层的节点值
        level_node = [root]
        while len(level_node) > 0:
            # 该列表用来保存每一层遍历的结果
            level_list = []
            # 该列表用来保存当前层的下一层节点集合
            next_node = []
            # 依次遍历当前层的每个节点
            for node in level_node:
                level_list.append(node.val)
                if node.left and node.left.val is not None:
                    next_node.append(node.left)
                if node.right and node.right.val is not None:
                    next_node.append(node.right)
            pre_list.append(level_list)
            level_node = next_node
        return pre_list
        

    # 根据给定的数组创建二叉树
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
    data = [0,2,4,1,None,3,-1,5,1,None,6,None,8]
    root = Solution().createBTree(data)
    pre_root = Solution().levelOrder(root)
    print(pre_root)

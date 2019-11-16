class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 此题难点：当前节点的左子树节点上的值必须恒小于其所有父节点的值
    # 关键点：中序遍历得到的值是单增的
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        root_list = []

        # 中序遍历
        def traverse(root):
            if root is None:
                return
            traverse(root.left)
            if root.val is not None:
                root_list.append(root.val)
            traverse(root.right)             
        traverse(root)
        print("root_list", root_list)
        root_copy = root_list[:]
        root_list.sort()
        return True if root_list==root_copy and len(set(root_list))==len(root_list) else False
            

    def createBTree(self, data, index=0):
        if len(data) == 0:
            return
        pNode = None
        if index < len(data):
            pNode = TreeNode(data[index])
            pNode.left = self.createBTree(data, 2*index+1)
            pNode.right = self.createBTree(data, 2*index+2)
        return pNode

    # 先序遍历
    def pretraverse(self, root):
        if root is not None:
            print(root.val)
            self.pretraverse(root.left)
            self.pretraverse(root.right)
        else:
            return

    # 层次遍历
    def layer_traverse(self, root):
        if root is None:
            return []
        queue = [root]
        output = []
        while queue:
            res = []
            nextQueue = []
            for point in queue:
                res.append(point.val)
                if point.left:
                    nextQueue.append(point.left)
                if point.right:
                    nextQueue.append(point.right)
            output.extend(res)
            queue = nextQueue
        return output


if __name__ == "__main__":
    root_list = [1, 1]
    root = Solution().createBTree(root_list)
    output = Solution().isValidBST(root)
    print(output)

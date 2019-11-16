class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        if root.left is None and root.right is None:
            return sum == root.val
        elif root.left is not None and root.right is None:
            return self.hasPathSum(root.left, sum-root.val)
        elif root.left is None and root.right is not None:
            return self.hasPathSum(root.right, sum-root.val)
        else:
            return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)


# 创建二叉树
def build(data):
    if len(data) == 0:
        return TreeNode(0)
    nodeQueue = []
    # 创建一根节点，并将根节点进栈
    root = TreeNode(data[0])
    nodeQueue.append(root)
    # 记录当前行节点的数量
    lineNum = 2
    # 记录当前行中数字在数组中的位置
    startIndex = 1
    # 记录数组中剩余元素的数量
    restLength = len(data) - 1
    while restLength > 0:
        for index in range(startIndex, startIndex + lineNum, 2):
            if index == len(data):
                return root
            cur_node = nodeQueue.pop()
            if data[index] is not None:
                cur_node.left = TreeNode(data[index])
                nodeQueue.append(cur_node.left)
            if index + 1 == len(data):
                return root
            if data[index + 1] is not None:
                cur_node.right = TreeNode(data[index + 1])
                nodeQueue.append(cur_node.right)
        startIndex += lineNum
        restLength -= lineNum
        # 此处用来更新下一层树对应节点的最大值
        lineNum = len(nodeQueue) * 2
    return root


if __name__ == "__main__":
    nums = [1,-2,-3,1,3,-2,None,-1]
    root = build(nums)
    target = 3
    have_path = Solution().hasPathSum(root, target)
    print(have_path)

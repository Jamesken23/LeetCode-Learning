class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        p_list = []
        def p_traverse(p):
            if p is None:
                return
            p_list.append(p.val)
            p_traverse(p.left)
            p_traverse(p.right)
        p_traverse(p)

        q_list = []
        def q_traverse(q):
            if q is None:
                return
            q_list.append(q.val)
            q_traverse(q.left)
            q_traverse(q.right)
        q_traverse(q)

        print("p_list", p_list)
        print("q_list", q_list)
        return True if p_list==q_list else False

    def createBTree(self, data, index=0):
        pNode = None
        if index < len(data):
            pNode = TreeNode(data[index])
            pNode.left = self.createBTree(data, 2*index+1)
            pNode.right = self.createBTree(data, 2*index+2)
        return pNode

    def preTraverse(self, root):
        if root is None:
            return
        print(root.val)
        self.preTraverse(root.left)
        self.preTraverse(root.right)


if __name__ == "__main__":
    p_list = [1, 2]
    q_list = [1, None, 2]
    p_node = Solution().createBTree(p_list)
    q_node = Solution().createBTree(q_list)
    is_same = Solution().isSameTree(p_node, q_node)
    print(is_same)

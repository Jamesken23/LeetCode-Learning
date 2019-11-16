class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 本题采用回溯法解决
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n==0:
            return []
        meno = dict()

        def back(left=1, right=n, meno=meno):
            if left > right:
                return [None]
            if (left, right) in meno:
                return meno[(left, right)]
            res = []
            for i in range(left, right+1):
                left_nodes = back(left, i-1, meno)
                right_nodes = back(i+1, right, meno)
                for left_node in left_nodes:
                    for right_node in right_nodes:
                        root = TreeNode(i)
                        root.left = left_node
                        root.right = right_node
                        res.append(root)
            meno[(left, right)] = res
            return res

        back()
        return meno[(1, n)]


if __name__ == "__main__":
    n = 3
    tree_list = Solution().generateTrees(n)
    print(tree_list)

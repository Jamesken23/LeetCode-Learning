class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder is None or inorder is None:
            return None
        # 定义一链表用来记录中序序列中元素的下标值
        dict_in = {}
        for index, value in enumerate(inorder):
            dict_in[value] = index
        length = len(preorder)-1

        # 使用深度遍历方法遍历
        def dfs(pre_start, pre_end, in_start, in_end, preorder,inorder,dict_in):
            if pre_end >= pre_start and in_end >= in_start:
                root = TreeNode(preorder[pre_start])
                # 求得根节点的val值在中序序列中的下标值
                mid_index = dict_in[preorder[pre_start]]
                # 分别求得左、右子树的长度
                l_len = mid_index - in_start
                r_len = in_end - mid_index
                # 求得根节点root的左子树
                root.left = dfs(pre_start+1,pre_start+l_len,in_start,
                                in_start+l_len-1, preorder, inorder,dict_in)
                root.right = dfs(pre_start+l_len+1,pre_start+l_len+r_len,mid_index+1,
                                mid_index+r_len, preorder, inorder,dict_in) 
                return root
        return dfs(0, length, 0, length, preorder, inorder, dict_in)
            

if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    BTree = Solution().buildTree(preorder, inorder)
    print(BTree)

class Solution(object):
    # 此题使用动态规划方法解决
    # 利用二叉树的性质 根节点选定i之后
    # 那么它的左子树的结点个数应该是 i -1;右子树的结点的个数应该是 n-i;
    # 它是个和的形式 因为它有i个分配方式
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        flag_list = [0]*(n+1)
        flag_list[0] = 1
        flag_list[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                flag_list[i] += flag_list[j]*flag_list[i-j-1]
        return flag_list[n]


if __name__ == "__main__":
    n = 1
    tree_nums = Solution().numTrees(n)
    print(tree_nums)

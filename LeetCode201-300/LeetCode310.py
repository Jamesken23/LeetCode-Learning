import collections

class Solution(object):
    # 本题使用DFS拓扑排序法；一直对度数为1的节点进行剪枝，直至剩余节点数小于3
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # 定义一字典，用来保存当前节点的相邻节点的集合
        neighbor_nodes = collections.defaultdict(list)
        # 定义一字典，用来记录当前节点的度数
        du_num = collections.defaultdict(int)
        for node in edges:
            neighbor_nodes[node[0]].append(node[0])
            neighbor_nodes[node[1]].append(node[1])
            du_num[node[0]] += 1
            du_num[node[1]] += 1
        one_list = list(range(n))
        while n > 2:
            for index in range(n):
                if du_num[index] == 1:
                    du_num[index] -= 1
                    for node_index in neighbor_nodes[index]:
                        du_num[node_index] -= 1
                    n -= 1
                    one_list.remove(index)
        return one_list
        


if __name__ == "__main__":
    n = 6
    edges = [[0,1],[0,2],[0,3],[3,4],[4,5]]
    min_node = Solution().findMinHeightTrees(n, edges)
    print(min_node)

import collections


class Solution(object):
    # 本题采用拓扑排序（DFS）方法
    def canFinish(self, N, prerequisites):
        """
        :type N,: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 需要定义两个字典；
        # 一个字典用来记录图中每个节点的后续节点
        # 一个字典用来记录当前节点的入度数
        next_node = collections.defaultdict(list)
        rudu_num = collections.defaultdict(int)
        for node in prerequisites:
            next_node[node[0]].append(node[1])
            rudu_num[node[1]] += 1
        start = 0
        finish = 0
        print("next_node", next_node)
        print("rudu_num", rudu_num)
        while start < N:
            # 如果当前节点入度为0，则将该节点的后续节点的入度数分别1
            if rudu_num[start] == 0:
                for node in next_node[start]:
                    rudu_num[node] -= 1
                rudu_num[start] = -1
                start = 0
                finish += 1
                continue
            if finish == N:
                return True
            start += 1
        print("next_node", next_node)
        print("rudu_num", rudu_num)
        return False


if __name__ == "__main__":
    N = 3
    prerequisites = [[0, 2], [1, 2], [2, 0]]
    is_finish = Solution().canFinish(N, prerequisites)
    print(is_finish)

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # 首先给每个孩子分配一颗糖果
        candy_list = [1]*len(ratings)
        candy_list.insert(0, 0)
        candy_list.append(0)
        # 首尾加上0，方便遍历首尾元素
        ratings.insert(0, 0)
        ratings.append(0)
        # 正向调整，如果当前孩子比之前孩子的分数高，
        # 那么令当前孩子的糖果数比之前孩子糖果数大1 res[i]=res[i-1]+1；
        for start in range(1, len(ratings)-1):
            if ratings[start] > ratings[start-1]:
                candy_list[start] = candy_list[start-1]+1
        # 反向调整，如果当前孩子比之前孩子的分数高，
        # 那么比较当前孩子的糖果数和之前孩子的糖果数+1，
        # 取更大的为当前孩子糖果数res[i]=max(res[i],res[i+1]+1)；
        for end in range(len(ratings)-2, 0, -1):
            if ratings[end] > ratings[end+1]:
                candy_list[end] = max(candy_list[end], candy_list[end+1]+1)
        return sum(candy_list)


if __name__ == "__main__":
    ratings = [1, 2, 2]
    candy_num = Solution().candy(ratings)
    print(candy_num)

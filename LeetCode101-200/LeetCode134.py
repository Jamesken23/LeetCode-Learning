class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        location = -1
        total_sum = 0
        # 如果每个站点加的油总量和小于消耗的总油量，则肯定环绕不了一周
        if sum(gas) < sum(cost):
            return location
        for index in range(len(gas)):
            total_sum += gas[index] - cost[index]
            if total_sum < 0:
                location = index+1
                total_sum = 0
        return location

if __name__ == "__main__":
    gas = [5,1,2,3,4]
    cost = [4,4,1,5,1]
    location = Solution().canCompleteCircuit(gas, cost)
    print(location)

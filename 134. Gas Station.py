from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = 0
        result = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                result = i + 1

        return result
    
a = Solution()
gas = [1,2,3,4,5] 
cost = [3,4,5,1,2]
sol = a.canCompleteCircuit(gas=gas, cost=cost)
print(sol)

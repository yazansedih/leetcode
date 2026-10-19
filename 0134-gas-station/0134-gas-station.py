class Solution(object):
    def canCompleteCircuit(self, gas, cost):

        start = 0
        current_tank = 0
        total_tank = 0

        # get start point
        for i in range(len(gas)): 
            diff = gas[i] - cost[i] 

            current_tank += diff
            total_tank += diff

            if current_tank < 0:
                start = i + 1
                current_tank = 0

        if total_tank < 0:
            return -1

        return start

        

        
                
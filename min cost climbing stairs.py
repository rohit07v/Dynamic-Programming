#You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

#You can either start from the step with index 0, or the step with index 1.

#Return the minimum cost to reach the top of the floor.
# cost = [10,15,20]
# output = 15


def min_cost_climb_stairs(cost):
    if not cost:
        return 0
    first = cost[0]
    second = cost[1]
    for i in range(2,len(cost)):
        curr = cost[i]+min(first,second)
        first = second
        second = curr
    return min(first,second)


    #first = 10
    #Second = 15
    # curr = 20+10 = 30
    #first = 15
    #second = 30
    # return min(15,30)
    

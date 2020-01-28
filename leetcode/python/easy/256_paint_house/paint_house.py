"""
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

Find the minimum cost to paint all houses.
"""

def paint(n, costs):
    """
    n - number of houses
    costs - The cost of painting each house with a certain color is represented
    by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting
    house 0 with color red; costs[1][2] is the cost of painting house 1 with
    color green, and so on.
    """

    """
    Recursive solution:

    Find the cheapest colour that is not beside the other.

    red cost = min(costs[i - 1][1], costs[i - 1][2]) + costs[i][0]
    blue cost = min(costs[i - 1][0], costs[i - 1][2]) + costs[i][1]
    green cost = min(costs[i - 1][0], costs[i - 1][1]]) + costs[i][2]

    If we are able to go through the entire costs matrix doing these calculations,
    it should allow the final cost list to contain the min final cost.

    """
    if not costs:
        return 0
    elif len(costs) < 2:
        return min(costs[0])

    for i in range(1, n):
        costs[i][0] = min(costs[i - 1][1], costs[i - 1][2]) + costs[i][0]
        costs[i][1] = min(costs[i - 1][0], costs[i - 1][2]) + costs[i][1]
        costs[i][2] = min(costs[i - 1][0], costs[i - 1][1]) + costs[i][2]

    return min(costs[-1])

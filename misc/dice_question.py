"""
A six-sided die is a small cube with a different number of pips on each face (side), ranging from 1 to 6.
On any two opposite side of the cube, the number of pips adds up to 7; that is, there are three pairs of opposite sides: 1 and 6, 2 and 5, and 3 and 4.
There are N dice lying on a table, each showing the pips on its top face. In one move, you can take one die and rotate it to an adjacent face.
For example, you can rotate a die that shows 1 s that it shows 2, 3, 4 or 5. However, it cannot show 6 in a single move, because the faces with one pip and six pips visible are opposite sides rather than adjacent.
You want to show the same number of pips on the top face of all N dice. Given that each of the dice can be moved multiple times, count the minimum number of moves needed to get equal faces.

Write a function that, given an array A consisting of N integers describing the number of pips (from 1 to 6) shown on each die's top face, returns the minimum number of moves necessary for each die show the same number of pips.
"""


def solution(dice):
    """
    Counts the number occurrences then calculates the min number of rolls from those occurrences by using the fact that
    if a dice is already at the face all the die are moving to then it requires zero rolls, if it's on the opposite face    it takes 2 rolls and every other face takes one roll.
    """
    # Setup hashmap for containing the number of occurrences.
    faces = dict(list(range(1,7)), 0)

    # Count the occurrences. O(N)
    for d in arr:
        faces[d] += 1

    # Check the rolls required to get all the die to each face.
    min_rolls = len(arr)
    for cur_face, occurrences in faces.items():
        min_rolls = min(min_rolls, len(arr) - occurrences + faces[7 - cur_face])

    return min_rolls

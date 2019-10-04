import unittest
from functools import cmp_to_key

def compare_func(x, y):
    if x[0] != y[0]:
        return x[0] - y[0]
    else:
        return x[1] + x[2] - y[1] - y[2]

# Sorts all lists based on first list
def sort_lists(list1, list2, list3):

    zipped_pairs = zip(list1, list2, list3)

    z = [x for x in sorted(zipped_pairs, key=cmp_to_key(compare_func))]

    return z

def kruskals(g_nodes, g_from, g_to, g_weight):

    g_weight, g_from, g_to = zip(*sort_lists(g_weight, g_from, g_to))

    visited = set()
    bunches = list()
    total_weight = 0

    for i in range(len(g_weight)):

        if len(bunches) == 1 and len(visited) == g_nodes:
            break

        # Add edge nodes to visited
        visited.add(g_from[i])
        visited.add(g_to[i])

        to_add = g_weight[i]
        noted_set = -1
        # Check if either of the nodes are in a set in bunches
        # If both are in the same set then don't add the weight else, add the weight
        # If one is in a set but not the other then add the other node to the set
        # If they are both in different sets then join the sets
        for j in range(len(bunches)):
            if g_from[i] in bunches[j] and g_to[i] in bunches[j]:
                to_add = 0
                noted_set = -2
                break

            if g_from[i] in bunches[j] or g_to[i] in bunches[j]:
                if noted_set == -1:
                    noted_set = j
                    bunches[j].add(g_from[i])
                    bunches[j].add(g_to[i])
                else:
                    bunches[noted_set] = bunches[noted_set].union(bunches[j])
                    del bunches[j]
                    break
            # if g_to[i] in bunches[j]:
            #     if noted_set == -1:
            #         noted_set  = j
            #     else:
        if noted_set == -1:
            bunches.append({g_from[i], g_to[i]})

        total_weight += to_add


    return total_weight

class BasicTests(unittest.TestCase):

    def test_1(self):
        # Get input
        text_input = open("input05.txt", 'r')
        lines = text_input.readlines()
        x = lines[0].split()
        g_nodes = x[0]
        n = x[1]
        text_input.close()

        del lines[0]

        g_from = list()
        g_to = list()
        g_weight = list()

        for line in lines:
            y = line.strip('\n').split(' ')
            g_from.append(int(y[0]))
            g_to.append(int(y[1]))
            g_weight.append(int(y[2]))

        # Get output
        output = 6359060
        #Check
        self.maxDiff = 10
        self.assertEqual(kruskals(g_nodes, g_from, g_to, g_weight), output)

if __name__ == '__main__':
    unittest.main()

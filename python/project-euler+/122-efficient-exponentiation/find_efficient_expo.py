"""
Output in string format the most efficient way to calculate the exponent n^k(minimize multiplications)

3
15
17
22

"""
import math

def print_num_multiplications(num):
    """
    Prints the number given on a new line.
    :param num: number to be printed
    """
    print(str(num))


def print_output_line(list_of_nums):
    """
    prints: n^a * n^b = n^c
    :param list_of_nums: list of exponents to be printed in the output should be in the form: [a, b, c]
    """
    print("n^" + str(list_of_nums[0]) + " * n^" + str(list_of_nums[1]) + " = n^" + str(list_of_nums[2]))

def print_output(spec_list):
    """
    Given the spec_list, prints out the number of multiplications then the steps for more efficient exponentiation
    :param spec_list: list containing a natural number to start, then a series of lists containing [a, b, c]
    """
    print_num_multiplications(spec_list[0])
    for i in range(1, len(spec_list)):
        print_output_line(spec_list[i])

# def gen_fibs(k):
#     fib = []
#     a = 1
#     b = 2
#     while a < k:
#         fib.append(a)
#         temp = a
#         a = b
#         b = b + temp
#     return fib

def binary_method(tasks):
    """
    Takes k and returns the spec list that specifies the steps to get the most efficient exponentiation.
    :param k: the input from the question (exponent to calculate)
    :return: list that has the specifications of how to get the most efficient exponentiation
    """
    for _ in range(tasks):
        steps = get_spec_method(int(input()))
        final_list = [len(steps)] + steps
        print_output(final_list)

def get_spec_method(k):
    """
    Recursive method for a simple, understandable way of finding the addition chain for input k
    :param k: result of addition chain
    :return: steps of addition chain
    """
    ret_list = list()
    b = 1
    while b <= k:
        a = b
        b = a * 2
        if b <= k:
            ret_list.append([a, a, b])

    remainder = k - a
    if remainder == 0:
        return ret_list
    elif remainder < 3:
        ret_list.append([a, remainder, k])
        return ret_list
    else:
        for x in get_spec_method(remainder):
            ret_list.append(x)
        ret_list.append([a, remainder, k])
        return ret_list

def power_tree_method(tasks):
    """
    Implements the power tree method for finding the best addition chain for input k
    :param method: number of tasks to do
    """
    tree = make_tree(23)
    for _ in range(tasks):
        chain = make_chain(tree, int(input()))
        steps = list_from_chain((chain))
        out = [len(steps)] + steps
        print_output(out)

def list_from_chain(chain):
    p = list()
    for i in range(1, len(chain)):
        p.append([chain[i - 1], (chain[i] - chain[i - 1]), chain[i]])
    return p

def make_chain(tree,x):
    """
    makes the chain using the tree and the input x
    :param tree: tree (map) to use
    :param x: value to input
    :return: list containing the steps to getting to x
    """
    c = [x]
    while x!=1:
        x=tree[x]
        c.append(x)
    return c[::-1]

def make_tree(levels):
    """
    Makes a tree
    :param levels:
    :return: a tree with levels according to the input
    """
    tree = {1:None}
    leaves = [1]
    for _ in range(levels):
        newleaves = []
        for leaf in leaves:
            for i in make_chain(tree,leaf):
                if (i + leaf) not in tree:
                    tree[i + leaf] = leaf
                    newleaves.append(i + leaf)
        leaves = newleaves
    return tree

if __name__ == "__main__":
    # binary_method(int(input()))
    power_tree_method(int(input()))




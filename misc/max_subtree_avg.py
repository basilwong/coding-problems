def max_avg(root):
    if not root:
        return None

    def helper(node):
        max_avg = None
        max_root = None
        cur_avg = node.val
        cur_num = 1

        for child in node.children:
            input = helper(child)
            if max_avg is None or max_avg < input[1]:
                max_avg = input[1]
                max_root = input[0]
            cur_num += input[3]
            cur_avg = (cur_avg + input[2]) / cur_num

        if max_avg == None or max_avg < cur_avg:
            max_avg = cur_avg
            max_root = node

        return [max_root, max_avg, cur_avg, cur_num]

    return helper[0]

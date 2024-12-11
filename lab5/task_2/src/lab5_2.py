from lab5.utils import open_file, write_file, measuring, print_input_output

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def build_tree(n, parents):
    tree = [[] for i in range(n)]
    root = None
    for child in range(n):
        parent = parents[child]
        if parent == -1:
            root = child
        else:
            tree[parent].append(child)
    return tree, root


def find_tree_height(tree, node):
    if not tree[node]:  # Если у узла нет детей
        return 1
    else:
        height = 0
        for child in tree[node]:
            height = max(height, find_tree_height(tree, child))
        return height + 1


def task_2(input_file, output_file):
    n, nums = open_file(input_file)
    inputs = (str(n) + "\n" + " ".join(map(str, nums)))
    tree, root = build_tree(n, nums)
    result = str(find_tree_height(tree, root))
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(find_tree_height, tree, root)


if __name__ == '__main__':
    task_2(PATH_INPUT, PATH_OUTPUT)

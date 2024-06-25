class Node:
    def __init__(self, key):
        self.key = key
        self.color = "black"  # default color
        self.left = None
        self.right = None
        self.parent = None


def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.key:
        left_child = insert(root.left, key)
        root.left = left_child
        left_child.parent = root
    else:
        right_child = insert(root.right, key)
        root.right = right_child
        right_child.parent = root

    return root


def level_order_traversal(root):
    if root is None:
        return []

    result = []
    queue = [root]

    while queue:
        current = queue.pop(0)
        result.append(current)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result


def is_valid_red_black_tree(root):
    def dfs(node, black_count, path_black_counts):
        if node is None:
            if black_count not in path_black_counts:
                path_black_counts.append(black_count)
            return len(path_black_counts) == 1

        if node.color == "black":
            black_count += 1
        elif node.color == "red":
            if (node.left and node.left.color == "red") or (node.right and node.right.color == "red"):
                return False

        return dfs(node.left, black_count, path_black_counts) and dfs(node.right, black_count, path_black_counts)

    return dfs(root, 0, [])


def all_possible_colorings(root):
    def backtrack(node):
        if node is None:
            if is_valid_red_black_tree(root):
                results.append(level_order_traversal(root))
            return

        if node != root:  # root must be black
            node.color = "black"
            backtrack(node.left)
            backtrack(node.right)
            node.color = "red"
            backtrack(node.left)
            backtrack(node.right)
        else:
            backtrack(node.left)
            backtrack(node.right)

    results = []
    root.color = "black"
    backtrack(root)
    return results


def print_trees(trees):
    for idx, tree in enumerate(trees):
        print(f"Tree {idx + 1}:")
        for node in tree:
            color = "Red" if node.color == "red" else "Black"
            print(f"Node {node.key}: {color}")
        print("\n")


# Example usage
if __name__ == "__main__":
    values = [10, 5, 20, 3, 7, 15, 30]
    root = None

    for value in values:
        root = insert(root, value)

    all_trees = all_possible_colorings(root)
    print_trees(all_trees)

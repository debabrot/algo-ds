from collections import deque

class TreeNode:
    """
    Tree data structure for tree with more then 2 nodes per child
    """
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self):
        return f"TreeNode({self.data})"

    def print_tree(self, level=0):
        prefix = "  " * level
        print(f"{prefix}- {self.data}")
        for child in self.children:
            child.print_tree(level + 1)


def bfs(root):
    if not root:
        return []

    queue = deque([root])
    visited = set()
    result = []
    visited.add(root)
    print(f"Starting BFS from node: {root.data}")
    print(queue, result, visited)

    while queue:
        current_node = queue.popleft()
        result.append(current_node.data)
        print(queue, result, visited)

        # Enqueue all unvisited children/neighbors
        for child in current_node.children:
            if child not in visited:
                visited.add(child)
                queue.append(child)
            print(queue, result, visited)
    return result


def max_height(root):
    if not root:
        return 0
    queue = deque([root])
    height = 0

    while queue:
        height += 1
        level_size = len(queue)
        print("pre", height, queue, level_size)
        for _ in range(level_size):
            current = queue.popleft()
            for child in current.children:
                queue.append(child)
        print("post", height, queue, level_size)


    return height
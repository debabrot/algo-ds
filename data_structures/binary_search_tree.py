from typing import Optional


class TreeNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


def insert(root: Optional[TreeNode], value: int) -> TreeNode:
    if root is None:
        return TreeNode(value)
    else:
        if root.value > value:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
    return root


def search(root: Optional[TreeNode], value: int) -> Optional[TreeNode]:
    if root is None or root.value == value:
        return root
    if root.value > value:
        return search(root.left, value)
    return search(root.right, value)



def print_preorder(root: Optional[TreeNode]) -> None:
    if root is None:
        return None
    print(root.value)
    print_preorder(root.left)
    print_preorder(root.right)


def print_inorder(root: Optional[TreeNode]) -> None:
    if root is None:
        return None
    print_inorder(root.left)
    print(root.value)
    print_inorder(root.right)


def print_postorder(root: Optional[TreeNode]) -> None:
    if root is None:
        return None
    print_postorder(root.left)
    print_postorder(root.right)
    print(root.value)


def find_min(root: TreeNode) -> TreeNode:
    current = root
    while current.left:
        current = current.left
    return current


def find_max(root: TreeNode) -> TreeNode:
    current = root
    while current.right:
        current = current.right
    return current


def successor(root: Optional[TreeNode], node: TreeNode) -> Optional[TreeNode]:
    if root is None:
        return None

    if node.right:
        return find_min(node.right)
    else:
        successor_node = None
        current = root
        while current:
            if current.value > node.value:
                successor_node = current
                current = current.left
            elif current.value < node.value:
                current = current.right
            else:
                break
        return successor_node


def predecessor(root: Optional[TreeNode], node: TreeNode) -> Optional[TreeNode]:
    if root is None:
        return None

    if node.left:
        return find_max(node.left)
    else:
        predecessor_node = None
        current = root
        while current:
            if current.value < node.value:
                predecessor_node = current
                current = current.right
            elif current.value > node.value:
                current = current.left
            else:
                break
        return predecessor_node


def delete(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if root is None:
        return None
    if root.value > key:
        root = delete(root.left, key)
    elif root.value < key:
        root = delete(root.right, key)
    else:
        if root.left is None and root.right is None:
            return None
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            successor = find_min(root.right)
            root.value = successor.value
            root.right = delete(root.right, successor.value)
        return root
    return root


def validate(root: Optional[TreeNode], low=float('-inf'), high=float('inf')) -> bool:
    if root is None:
        return True

    if not low < root.value < high:
        return False
    return (validate(root.left, low, root.value) and
            validate(root.right, root.value, high))


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None
    
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root

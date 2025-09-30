class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insert a value into the BST
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    # Search for a value in the BST
    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    # In-order traversal (Left -> Root -> Right)
    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)


# Example usage
bst = BST()
values = [50, 30, 70, 20, 40, 60, 80]

for v in values:
    bst.insert(v)

print("In-order traversal:", bst.inorder())  # Sorted order
print("Search 40:", bst.search(40))  # True
print("Search 25:", bst.search(25))  # False


def delete(root, key):
    if root is None:
        return None

    # First, find the node to delete
    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:  # Found the node to delete

        # Case 1: No children
        if root.left is None and root.right is None:
            return None
        # Case 2: One child
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # Case 3: Two children
        else:
            # Find inorder successor (smallest in right subtree)
            successor = find_min(root.right)
            root.data = successor.data
            root.right = delete(root.right, successor.data)
    
    return root

def find_min(node):
    current = node
    while current.left:
        current = current.left
    return current

def successor(root, node):
    if root is None or node is None:
        return None
    
    # Case 1: Node has right subtree
    if node.right:
        current = node.right
        while current.left:
            current = current.left
        return current
    
    # Case 2: No right subtree - find ancestor
    successor_node = None
    current = root
    while current:
        if current.data > node.data:
            successor_node = current
            current = current.left
        elif current.data < node.data:
            current = current.right
        else:
            break
    return successor_node

def predecessor(root, node):
    if root is None or node is None:
        return None
    
    # Case 1: Node has left subtree
    if node.left:
        current = node.left
        while current.right:
            current = current.right
        return current
    
    # Case 2: No left subtree - find ancestor
    predecessor_node = None
    current = root
    while current:
        if current.data < node.data:
            predecessor_node = current
            current = current.right
        elif current.data > node.data:
            current = current.left
        else:
            break
    return predecessor_node
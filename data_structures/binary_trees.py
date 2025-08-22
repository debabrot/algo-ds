class BinaryTreeNode:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

def dfs_inorder(root):
    if root:
        dfs_inorder(root.left)
        print(root.value, end=' ')
        dfs_inorder(root.right)

def dfs_preorder(root):
    if root:
        print(root.value, end=' ')
        dfs_preorder(root.left)
        dfs_preorder(root.right)

def dfs_postorder(root):
    if root:
        dfs_postorder(root.left)
        dfs_postorder(root.right)
        print(root.value, end=' ')


def max_height(root):
    if root:
        max_left = max_height(root.left)
        max_right = max_height(root.right)
        return 1 + max(max_left, max_right)
    else:
        return 0
class TreeNode:
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


# Let's create a simple tree
root = TreeNode("Electronics")
laptops = TreeNode("Laptops")
phones = TreeNode("Phones")
desktops = TreeNode("Desktops")

root.add_child(laptops)
root.add_child(phones)
root.add_child(desktops)

macbook = TreeNode("MacBook Air")
dell = TreeNode("Dell XPS")
laptops.add_child(macbook)
laptops.add_child(dell)

iphone = TreeNode("iPhone 15")
android = TreeNode("Samsung Galaxy")
phones.add_child(iphone)
phones.add_child(android)

# Print the tree
print("--- Electronics Tree ---")
root.print_tree()
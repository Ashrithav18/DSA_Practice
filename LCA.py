class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def lowestCommonAncestor(root, p, q):

    while root:

        # both in left
        if p.val < root.val and q.val < root.val:
            root = root.left

        # both in right
        elif p.val > root.val and q.val > root.val:
            root = root.right

        else:
            return root   # split point (LCA)
# Build BST
root = Node(6)
root.left = Node(2)
root.right = Node(8)
root.left.left = Node(0)
root.left.right = Node(4)
root.right.left = Node(7)
root.right.right = Node(9)

p = root.left   # 2
q = root.right  # 8

lca = lowestCommonAncestor(root, p, q)

print(lca.val)
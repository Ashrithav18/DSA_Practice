class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isIsomorphic(root1, root2):

    # Case 1: both empty
    if root1 is None and root2 is None:
        return True

    # Case 2: one is empty
    if root1 is None or root2 is None:
        return False

    # Case 3: values different
    if root1.data != root2.data:
        return False

    # Case 1: No swap
    no_swap = (isIsomorphic(root1.left, root2.left) and
               isIsomorphic(root1.right, root2.right))

    # Case 2: Swap
    swap = (isIsomorphic(root1.left, root2.right) and
            isIsomorphic(root1.right, root2.left))

    return no_swap or swap
# Tree 1
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)

# Tree 2
root2 = Node(1)
root2.left = Node(3)
root2.right = Node(2)

# Calling function
result = isIsomorphic(root1, root2)

print(result)
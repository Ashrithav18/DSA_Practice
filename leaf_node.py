class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def checkLeavesSameLevel(root):

    leaf_level = [-1]  # to store first leaf level

    def dfs(node, level):

        if node is None:
            return True

        # if leaf node
        if not node.left and not node.right:

            # first leaf
            if leaf_level[0] == -1:
                leaf_level[0] = level
                return True

            # check level
            return level == leaf_level[0]

        # check left and right
        return dfs(node.left, level + 1) and dfs(node.right, level + 1)

    return dfs(root, 0)


# Function Call
root = Node(1)
root.left = Node(2)
root.right = Node(3)

print(checkLeavesSameLevel(root))
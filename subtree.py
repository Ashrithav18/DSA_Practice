class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(a, b):
    if not a and not b:
        return True

    if not a or not b:
        return False

    if a.val != b.val:
        return False

    return isSameTree(a.left, b.left) and isSameTree(a.right, b.right)


def isSubtree(root, subRoot):

    if not root:
        return False

    if isSameTree(root, subRoot):
        return True

    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


# Function Call Example

root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

print(isSubtree(root, subRoot))
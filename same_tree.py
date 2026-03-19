class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isSameTree(p, q):

    # both empty
    if p is None and q is None:
        return True

    # one empty
    if p is None or q is None:
        return False

    # value check
    if p.data != q.data:
        return False

    # check left and right
    return (isSameTree(p.left, q.left) and
            isSameTree(p.right, q.right))
# Tree 1
p = Node(1)
p.left = Node(2)
p.right = Node(3)

# Tree 2
q = Node(1)
q.left = Node(2)
q.right = Node(3)

print(isSameTree(p, q))
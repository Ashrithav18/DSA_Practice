class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def findPreSuc(root, key):
    pred = None
    succ = None

    while root:

        if root.data == key:

            # find predecessor (max in left subtree)
            if root.left:
                temp = root.left
                while temp.right:
                    temp = temp.right
                pred = temp

            # find successor (min in right subtree)
            if root.right:
                temp = root.right
                while temp.left:
                    temp = temp.left
                succ = temp

            break

        elif key < root.data:
            succ = root
            root = root.left

        else:
            pred = root
            root = root.right

    return pred, succ


# ----------- MAIN PROGRAM -----------

# Create BST
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

key = 65

pred, succ = findPreSuc(root, key)

# Print results
print("Predecessor:", pred.data if pred else None)
print("Successor:", succ.data if succ else None)
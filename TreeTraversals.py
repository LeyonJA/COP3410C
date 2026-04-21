# Python program for preorder traversals
# Credit: geekforgeeks.org

# Structure of a Binary Tree Node
class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None

# Function to print preorder traversal
def printPreorder(node):
    if node is None:
        return

    # Deal with the node
    print(node.data, end=' ')

    # Recur on left subtree
    printPreorder(node.left)

    # Recur on right subtree
    printPreorder(node.right)

def printPostorder(node):
    if node == None:
        return

    # First recur on left subtree
    printPostorder(node.left)

    # Then recur on right subtree
    printPostorder(node.right)

    # Now deal with the node
    print(node.data, end=' ')

def printInorder(node):
    if node is None:
        return

    # First recur on left subtree
    printInorder(node.left)

    # Now deal with the node
    print(node.data, end=' ')

    # Then recur on right subtree
    printInorder(node.right)

# Driver code
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    # Function call
    print("Preorder traversal of binary tree is:")
    printPreorder(root)

    # Function call
    print("Postorder traversal of binary tree is:")
    printPostorder(root)

    # Function call
    print("Inorder traversal of binary tree is:")
    printInorder(root)

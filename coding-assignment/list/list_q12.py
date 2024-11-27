#Kth Smallest Element in a BST

def kth_smallest(root, k):
    def inorder_traversal(node):
        if not node:
            return []
        return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
    return inorder_traversal(root)[k - 1]

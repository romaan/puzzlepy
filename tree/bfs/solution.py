from collections import deque

class TreeNode:
    """
    A basic binary tree node.

    >>> node = TreeNode(10)
    >>> node.data
    10
    >>> node.left is None
    True
    >>> node.right is None
    True
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bfs_traversal(root):
    """
    Perform Breadth-First Search (level-order traversal)
    on a binary tree.

    >>> bfs_traversal(None)
    []

    Single node tree:
    >>> root = TreeNode(1)
    >>> bfs_traversal(root)
    [1]

    Complete binary tree:
            1
          /   \
         2     3
        / \   /
       4   5 6

    >>> root = TreeNode(1)
    >>> root.left = TreeNode(2)
    >>> root.right = TreeNode(3)
    >>> root.left.left = TreeNode(4)
    >>> root.left.right = TreeNode(5)
    >>> root.right.left = TreeNode(6)
    >>> bfs_traversal(root)
    [1, 2, 3, 4, 5, 6]
    """
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        current = queue.popleft()
        result.append(current.data)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result


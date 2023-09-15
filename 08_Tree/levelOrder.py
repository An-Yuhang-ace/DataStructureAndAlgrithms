from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        ans = []
        if root == None:
            return ans
        queue = deque([])
        queue.append(root)
        while len(queue) != 0:
            layer = []
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                layer.append(node.val)
                if node.left != None:
                    queue.append(node.left) 
                if node.right != None:
                    queue.append(node.right)
            ans.append(layer)
        return ans
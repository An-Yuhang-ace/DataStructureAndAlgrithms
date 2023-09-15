# Tree + DP
import sys

class treeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

def is_x2(x, y):
    d = int((x * y) ** 0.5)
    return d * d == x * y

def dfs(node):
    dp1, dp0 = 0, 0
    if node == None:
        return dp0, dp1
    for child in node.children:
        c0, c1 = dfs(child)
        if is_x2(node.val, child.val):
            dp1 = max(dp1, c0+2)
        dp0 = max(dp0, max(c0, c1))
    return dp0, dp1

if __name__ == "__main__":
    # initialize tree and input
    n = int(input())
    a = []
    a.append(treeNode(0))
    map = {}

    line = input()
    line = [int(s) for s in line.split()]
    for val in line:
        a.append(treeNode(val))

    for _ in range(n-1):
        line = input()
        line = [int(s) for s in line.split()]
        a[line[0]].children.append(a[line[1]])

    # dfs calculate dp
    dp0, dp1 = dfs(a[1])

    print(max(dp0, dp1))

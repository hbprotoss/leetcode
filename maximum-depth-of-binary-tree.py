#!/usr/bin/env python

"""
https://oj.leetcode.com/problems/maximum-depth-of-binary-tree/

Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def __init__(self):
        self.max_depth = 0

    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        self.func(root, 0)
        return self.max_depth

    def func(self, node, depth):
        if node == None:
            if depth > self.max_depth:
                self.max_depth = depth
            return

        self.func(node.left, depth+1)
        self.func(node.right, depth+1)
